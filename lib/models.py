from peewee import *
from lib.config import CONFIG
import base64

Database = SqliteDatabase(CONFIG["Database"])

class MetaModel(Model):
    class Meta:
        database = Database

class Artist(MetaModel):
    Title = CharField()
    MBID = CharField(null=True)

class Album(MetaModel):
    Title = CharField()
    Artist = ForeignKeyField(Artist, backref='Albums')
    ArtLarge = BlobField()
    ArtSmall = BlobField()
    MBID = CharField(null=True)

class Song(MetaModel):
    Album = ForeignKeyField(Album, backref='Songs')
    Title = CharField()
    Artist = ForeignKeyField(Artist, backref='Songs')
    TrackNumber = IntegerField()
    Path = CharField()

    def GetEncodedFile(self):
        with open(self.Path, "rb") as SongFile:
            return "data:audio/flac;base64," + base64.b64encode(SongFile.read()).decode('utf-8')

Database.connect()
Database.create_tables([Song, Album, Artist])