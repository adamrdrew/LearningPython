import os
from xmlrpc.client import Boolean
import mutagen
from mutagen import MutagenError
from peewee import *
from labler.config import CONFIG
import pdb
import functools

Database = SqliteDatabase(CONFIG["Database"])
Database.connect()

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
        return {
            "album" : self.GetTag("album"),
            "title" : self.GetTag("title"),
            "artist" : self.GetTag("artist"),
            "path" : self.Path,
            "tracknumber" : self.GetTag("tracknumber")
        }

class MusicScanner:
    def __init__(self, LibraryDir) -> None:
        self.LibraryDir = LibraryDir
        self.ScanCount = 0

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
        if songfile.LoadError: return
        ScannedSong = Song(songfile)
        ScannedSong.save()
        self.ScanCount += 1

    def __IsFileSupported(self, Path) -> Boolean:
        split = os.path.splitext(Path)
        if split == False: return False
        if len(split) != 2: return False
        extension = split[1].lower()
        for SupportedFile in CONFIG["SupportedFiles"]:
            if extension == SupportedFile: return True    
        return False

class Song(Model):
    Album = CharField()
    Title = CharField()
    Artist = CharField()
    TrackNumber = IntegerField()
    Path = CharField()

    class Meta:
        database = Database

    def __init__(self, SongFile):
            Metadata = SongFile.ToDict()
            print(Metadata)
            self.Album = Metadata["album"]
            self.Title = Metadata["title"]
            self.Artist = Metadata["artist"]
            self.TrackNumber = Metadata["tracknumber"]
            self.Path = Metadata["Path"]

