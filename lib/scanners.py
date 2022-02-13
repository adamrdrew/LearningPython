import musicbrainzngs
from lib.models import Album, Artist, Song
import base64
from lib.config import CONFIG
import os
from lib.scannerlib import UnknownAlbumImages, SongFile

class AlbumArtScanner:
    def __init__(self):
        musicbrainzngs.set_useragent(CONFIG["MusicBrains"]["Name"], CONFIG["MusicBrains"]["Version"], CONFIG["MusicBrains"]["Contact"])
        self.Debug = False

    def ScanLibrary(self):
        Albums = Album.select()
        [self.__FindAlbum(album) for album in Albums]

    def __FindAlbum(self, album):
        if self.Debug: print("Getting: " + album.Title)
        results = musicbrainzngs.search_releases(
            artist=album.Artist.Title,
            release=album.Title,
            limit=1)
        if len(results['release-list']) == 0: return
        MBAlbum = results['release-list'][0]
        album.MBID = MBAlbum["id"]
        try:
            self.__FindArt(album)
        except musicbrainzngs.musicbrainz.ResponseError:
            if self.Debug: print("Error")
            pass
        album.save()

    def __FindArt(self, album):
        album.ArtLarge = base64.b64encode(musicbrainzngs.get_image(mbid=album.MBID, coverid="front", size=CONFIG["MusicBrains"]["ImageSizeLarge"])).decode('utf-8')
        album.ArtSmall = base64.b64encode(musicbrainzngs.get_image(mbid=album.MBID, coverid="front", size=CONFIG["MusicBrains"]["ImageSizeSmall"])).decode('utf-8')

class MusicScanner:
    def __init__(self, LibraryDir) -> None:
        self.LibraryDir = LibraryDir
        self.ScanCount = 0
        self.ScanErrorCount = 0
        self.Debug = False
        self.UnknownAlbumImages = UnknownAlbumImages()

    def ScanLibrary(self) -> None:
        self.__ScanDir(self.LibraryDir)
        if self.Debug == False: return
        print("Files scanned: " + str(self.ScanCount))
        print("Error count: " + str(self.ScanErrorCount))

    #Private Methods
    def __GetFileList(self, Path) -> list:
        return [Filename for Filename in os.listdir(Path) if os.path.isfile(Path + Filename)]
    
    def __GetDirList(self, Path) -> list:
        return [Filename for Filename in os.listdir(Path) if os.path.isdir(Path + Filename)]

    
    def __ScanDir(self, Path):
        Dirs = self.__GetDirList(Path + "/")
        if Dirs != False: [self.__ScanDir(Path + "/" + Dir) for Dir in Dirs]
        Files = self.__GetFileList(Path + "/")
        if Files != False: [self.__ScanFile(Path + "/" + File) for File in Files]

    def __ScanFile(self, Path):
        if self.__IsFileSupported(Path) == False: return
        songfile = SongFile(Path)
        songDict = songfile.ToDict()
        if songfile.LoadError: 
            self.ScanErrorCount += 1
            return
        self.__AddToDatabase(songDict)
        self.ScanCount += 1
        if self.Debug: print("Song " + str(self.ScanCount) +" scanned: " + songDict["title"])

    def __AddToDatabase(self,songDict):
        #The indexes on the end of the get_or_create calls are because
        #it returns a tuple with the model in 0 and a status code in 1
        ScannedArtist = Artist.get_or_create(Title=songDict["artist"])[0]
        ScannedAlbum = Album.get_or_create(
            Title=songDict["album"], 
            Artist=ScannedArtist,
            ArtSmall=self.UnknownAlbumImages.EncodedImageSmall,
            ArtLarge=self.UnknownAlbumImages.EncodedImageLarge,
        )[0]
        ScannedSong = Song.get_or_create(
            Title=songDict["title"],
            TrackNumber=songDict["tracknumber"],
            Path=songDict["path"],
            Artist=ScannedArtist,
            Album=ScannedAlbum
        )[0]
        ScannedArtist.save()
        ScannedAlbum.save()
        ScannedSong.save()

    def __IsFileSupported(self, Path):
        split = os.path.splitext(Path)
        if split == False: return False
        if len(split) != 2: return False
        extension = split[1].lower()
        for SupportedFile in CONFIG["SupportedFiles"]:
            if extension == SupportedFile: return True    
        return False
