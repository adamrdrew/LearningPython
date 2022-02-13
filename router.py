import pdb

from flask import Flask, jsonify
from flask_cors import CORS,cross_origin
app = Flask( __name__ )
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

from lib.models import Album, Artist, Song

@app.route('/artist/by/title/<title>')
def GetArtistByName(title):
    artist = Artist.get(Artist.Title == title)
    RetVal = {
        "Title": title,
        "ID": artist.id,
        "Albums": [album.Title for album in artist.Albums]
    }
    return jsonify(RetVal)

@app.route('/artist/by/id/<id>')
def GetArtistByID(id):
    artist = Artist.get(id=id)
    RetVal = {
        "Title": artist.Title,
        "ID": artist.id,
        "Albums": [{
            "title":album.Title, 
            "id":album.id,
            "ArtSmall":"data:image/jpg;base64,"+album.ArtSmall.decode()
        } for album in artist.Albums]
    }
    return jsonify(RetVal)

@app.route('/api/artist/<id>')
def APIArtist(id):
    artist = Artist.get(id=id)
    ArtistInfo = {
        "Title": artist.Title,
        "ID": artist.id,
        "Albums": [{
            "Title":album.Title, 
            "Id":album.id,
            "ArtSmall":"data:image/jpg;base64,"+album.ArtSmall.decode()
        } for album in artist.Albums]
    }
    return jsonify(ArtistInfo)

@app.route('/api/album/<id>')
def APIAlbum(id):
    album = Album.get(id=id)
    AlbumInfo = {
        "Title":album.Title, 
        "Id":album.id,
        "ArtLarge":"data:image/jpg;base64,"+album.ArtLarge.decode(),
        "Artist": {
            "ID": album.Artist.id,
            "Title": album.Artist.Title
        },
        "Songs": [{
            "Title":song.Title, 
            "Id":song.id,
        } for song in album.Songs]
    }
    return jsonify(AlbumInfo)

@app.route('/api/album/all')
def APIAllAlbums():
    AlbumResults = Album.select()
    AlbumsInfo = [{
            "Title":album.Title, 
            "ID":album.id,
            "Artist": {
                "ID": album.Artist.id,
                "Title": album.Artist.Title
            },
            "ArtSmall":"data:image/jpg;base64,"+album.ArtSmall.decode()
        } for album in AlbumResults]
    return jsonify(AlbumsInfo)

if __name__ == '__main__':
        app.run()
