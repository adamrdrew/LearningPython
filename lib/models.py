from peewee import *
from lib.config import CONFIG

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

Database.connect()
Database.create_tables([Song, Album, Artist])