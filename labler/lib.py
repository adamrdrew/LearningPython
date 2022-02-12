import os
from xmlrpc.client import Boolean
import mutagen
from mutagen import MutagenError
from peewee import *
from labler.config import CONFIG
import pdb
import functools

Database = SqliteDatabase(CONFIG["Database"])


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

    def ScanLibrary(self) -> None:
        self.__ScanDir(self.LibraryDir)

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
        ScannedSong = Song.Create(songDict)
        ScannedSong.save()
        self.ScanCount += 1
        print("Song " + str(self.ScanCount) +" scanned: " + ScannedSong.Title)

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

class Song(MetaModel):
    Album = CharField()
    Title = CharField()
    Artist = CharField()
    TrackNumber = IntegerField()
    Path = CharField()

    @classmethod
    def Create(Class, SongDict):
            model = Class(
                Album=SongDict["album"], 
                Title=SongDict["title"],
                Artist=SongDict["artist"],
                TrackNumber=SongDict["tracknumber"],
                Path=SongDict["path"])
            return model

class Album(MetaModel):
    Title = CharField()
    Artist = CharField()
    ArtLarge = BlobField()
    ArtSmall = BlobField()
    About = CharField()

class Artist(MetaModel):
    Title = CharField()
    ArtSmall = BlobField()
    ArtLarge = BlobField()
    About = CharField()

Database.connect()
Database.create_tables([Song])


