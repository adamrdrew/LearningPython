import os
from xmlrpc.client import Boolean
import mutagen
from mutagen import MutagenError
from peewee import *
from labler.config import CONFIG
import pdb
import functools
import musicbrainzngs
import base64

Database = SqliteDatabase(CONFIG["Database"])

class UnknownAlbumImages:
    def __init__(self):
        self.PathSmall = "images/UnknownAlbumSmall.jpg"
        self.PathLarge = "images/UnknownAlbumLarge.jpg"
        self.EncodedImageLarge = self.__GetEncodedImage(self.PathLarge)
        self.EncodedImageSmall = self.__GetEncodedImage(self.PathSmall)
        pass

    def __GetEncodedImage(self, Path):
        with open(Path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode('utf-8')

class RouteManager:
    def __init__(self) -> None:
        self.messages = Messages()

    def root(self, args):
        return self.messages.root()

    def greet(self, name):
        return self.messages.greet(name)

class Messages:
    def __init__(self) -> None:
        pass

    def root(self):
        return "Hello from app"

    def greet(self, name):
        return "Hi " + name + " good to meet you!"

class SongFile:
    def __init__(self, Path):
        self.Path = Path
        self.TagIndex = 0
        self.LoadError = False
    
    @functools.cache
    def File(self):
        try:
            File = mutagen.File(self.Path)
        except MutagenError:
            self.LoadError = True
            File = {}
        return File

    def GetTag(self, Tag):
        return self.File()[Tag][self.TagIndex]

    def ToDict(self):
        try:
            return {
                "album" : self.GetTag("album"),
                "title" : self.GetTag("title"),
                "artist" : self.GetTag("artist"),
                "path" : self.Path,
                "tracknumber" : self.GetTag("tracknumber")
            }
        except KeyError:
            self.LoadError = True
            return {}

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

    def __IsFileSupported(self, Path) -> Boolean:
        split = os.path.splitext(Path)
        if split == False: return False
        if len(split) != 2: return False
        extension = split[1].lower()
        for SupportedFile in CONFIG["SupportedFiles"]:
            if extension == SupportedFile: return True    
        return False

class MetaModel(Model):
    class Meta:
        database = Database

class Artist(MetaModel):
    Title = CharField()
    #ArtSmall = BlobField()
    #ArtLarge = BlobField()
    #About = CharField()



class Album(MetaModel):
    Title = CharField()
    Artist = ForeignKeyField(Artist, backref='Albums')
    ArtLarge = BlobField()
    ArtSmall = BlobField()
    #About = CharField()

    @functools.cache
    def __MusicBrainzData(self):
        query="album:" + self.Title + " artist:" + self.Artist.Title
        results = musicbrainzngs.search_releases(query=query)
        return results["release-list"][0]

    @functools.cache
    def MBID(self):
        return self.__MusicBrainzData()["id"]

class Song(MetaModel):
    Album = ForeignKeyField(Album, backref='Songs')
    Title = CharField()
    Artist = ForeignKeyField(Artist, backref='Songs')
    TrackNumber = IntegerField()
    Path = CharField()

Database.connect()
Database.create_tables([Song, Album, Artist])


