import spotipy
import json
import os

from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyOAuth

scope = 'user-library-read playlist-read-private playlist-read-collaborative user-follow-read'

load_dotenv()
CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')
EXPORT_USERNAME = os.getenv('EXPORT_USERNAME')

redirect_uri = 'http://localhost'

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope=scope,
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        username=EXPORT_USERNAME,
        redirect_uri='http://localhost'
    )
)

library = {
    'ordered_playlists': list(),
    'user_playlists': list(),
    'followed_playlists': list(),
    'saved_albums': list(),
    'saved_tracks': list(),
    'followed_artists': list(),
}

playlists = sp.current_user_playlists()

while True:
    for playlist in playlists['items']:
        library['ordered_playlists'].append(playlist['id'])
        if playlist['owner']['id'] == EXPORT_USERNAME:
            library['user_playlists'].append(playlist['id'])
        else:
            library['followed_playlists'].append(playlist['id'])
    if not playlists['next']:
        break
    playlists = sp.next(playlists)

saved_albums = sp.current_user_saved_albums()

while True:
    for album in saved_albums['items']:
        library['saved_albums'].append(album['album']['id'])
    if not saved_albums['next']:
        break
    saved_albums = sp.next(saved_albums)

saved_tracks = sp.current_user_saved_tracks()

while True:
    for track in saved_tracks['items']:
        library['saved_tracks'].append(track['track']['id'])
    if not saved_tracks['next']:
        break
    saved_tracks = sp.next(saved_tracks)

followed_artists = sp.current_user_followed_artists()

while True:
    followed_artists = followed_artists['artists']
    for artist in followed_artists['items']:
        library['followed_artists'].append(artist['id'])
    if not followed_artists['next']:
        break
    followed_artists = sp.next(followed_artists)

with open('exported_data.json', 'w') as jf:
    json.dump(library, jf)
