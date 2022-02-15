from flask import Flask, jsonify
from flask_cors import CORS,cross_origin
app = Flask( __name__ )
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

from lib.controller import Controller
route_controller = Controller()

@app.route('/api/artist/<id>')
def get_artist(id):
    artist = route_controller.get_artist(id)
    return jsonify(artist)

@app.route('/api/artist/all')
def get_artists():
    artists = route_controller.get_artists()
    return jsonify(artists)

@app.route('/api/album/<id>')
def get_album(id):
    album = route_controller.get_album(id)
    return jsonify(album)

@app.route('/api/album/all')
def get_albums():
    albums = route_controller.get_albums()
    return jsonify(albums)

@app.route('/api/song/<id>')
def get_song(id):
    song = route_controller.get_song(id)
    return jsonify(song)

@app.route('/api/song/all')
def get_songs():
    songs = route_controller.get_songs()
    return jsonify(songs)

if __name__ == '__main__':
        app.run()
