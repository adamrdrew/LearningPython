import functools
import mutagen
from mutagen import MutagenError
import base64
from lib.config import CONFIG

class UnknownAlbumImages:
    def __init__(self):
        self.PathSmall = CONFIG["UnknownAlbumImagePaths"]["Small"]
        self.PathLarge = CONFIG["UnknownAlbumImagePaths"]["Large"]
        self.EncodedImageLarge = self.__GetEncodedImage(self.PathLarge)
        self.EncodedImageSmall = self.__GetEncodedImage(self.PathSmall)
        pass

    def __GetEncodedImage(self, Path):
        with open(Path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode('utf-8')

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
                "artist" : self.GetTag("albumartist"),
                "path" : self.Path,
                "tracknumber" : self.GetTag("tracknumber")
            }
        except KeyError:
            self.LoadError = True
            return {}