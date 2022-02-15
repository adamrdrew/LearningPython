from lib.models import Album, Artist, Song

class Controller:
    def __init__(self) -> None:
        pass

    def get_artist(self, id):
        artist = Artist.get(id=id)
        artist_info = {
            "title": artist.Title,
            "id": artist.id,
            "albums": [{
                "title":album.Title, 
                "id":album.id,
                "art_small":"data:image/jpg;base64,"+album.ArtSmall.decode()
            } for album in artist.Albums]
        }
        return artist_info

    def get_artists(self):
        artists = Artist.select()
        artist_info = [{
            "title": artist.Title,
            "id": artist.id,
            "albums": [{
                "title":album.Title, 
                "id":album.id,
                "art_small":"data:image/jpg;base64,"+album.ArtSmall.decode()
            } for album in artist.Albums]} for artist in artists]
        return artist_info

    def get_album(self, id):
        album = Album.get(id=id)
        album_info = {
            "title":album.Title, 
            "id":album.id,
            "art_small":"data:image/jpg;base64,"+album.ArtLarge.decode(),
            "artist": {
                "id": album.Artist.id,
                "title": album.Artist.Title
            },
            "songs": [{
                "title":song.Title, 
                "id":song.id,
            } for song in album.Songs]
        }
        return album_info

    def get_albums(self):
        albums = Album.select()
        albums_info = [{
                "title":album.Title, 
                "id":album.id,
                "artist": {
                    "id": album.Artist.id,
                    "title": album.Artist.Title
                },
                "art_small":"data:image/jpg;base64,"+album.ArtSmall.decode()
            } for album in albums]
        return albums_info

    def get_song(self, id):
            song_result = Song.get(id=id)
            song_info = {
                "title": song_result.Title,
                "id": song_result.id,
                "path": song_result.Path,
                "music_stream": song_result.GetEncodedFile(),
                "artist": {
                    "id": song_result.Artist.id,
                    "title": song_result.Artist.Title
                },
                "album": {
                    "id": song_result.Album.id,
                    "title": song_result.Album.Title,
                    "art_small": "data:image/jpg;base64,"+song_result.Album.ArtSmall.decode()
                },            
            }
            return song_info

    def get_songs(self):
            song_result = Song.select()
            song_info = [{
                "title": song.Title,
                "id": song.id,
                "path": song.Path,
                "artist": {
                    "id": song.Artist.id,
                    "title": song.Artist.Title
                },
                "album": {
                    "id": song.Album.id,
                    "title": song.Album.Title,
                },            
            } for song in song_result]
            return song_info
