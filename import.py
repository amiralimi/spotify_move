import spotipy
import json
import os
import base64
import requests
import time

from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyOAuth

scope = 'playlist-modify-public playlist-modify-private user-follow-modify user-library-modify ugc-image-upload'

load_dotenv()
CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')
IMPORT_USERNAME = os.getenv('IMPORT_USERNAME')

redirect_uri = 'http://localhost'

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope=scope,
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        username=IMPORT_USERNAME,
        redirect_uri='http://localhost'
    )
)

with open('exported_data.json', 'r') as jf:
    library = json.load(jf)

total = len(library['followed_artists'])
for i in range(0, total, 50):
    batch = library['followed_artists'][i: min(i + 50, total)]
    sp.user_follow_artists(ids=batch)

saved_tracks = library['saved_tracks']
saved_tracks.reverse()
# total = len(library['saved_tracks'])
# for i in range(0, 50, 50):
#     batch = saved_tracks[i:min(i + 50, total)]
#     sp.current_user_saved_tracks_add(tracks=batch)
#     time.sleep(1)
for track_id in saved_tracks:
    sp.current_user_saved_tracks_add(tracks=[track_id])
    time.sleep(0.1)

total = len(library['saved_albums'])
for i in range(0, total, 50):
    batch = library['saved_albums'][i:min(i + 50, total)]
sp.current_user_saved_albums_add(albums=batch)

library['ordered_playlists'].reverse()
playlist_map = []
for playlist_id in library['ordered_playlists']:
    if playlist_id in library['followed_playlists']:
        sp.current_user_follow_playlist(playlist_id=playlist_id)
    else:
        playlist = sp.playlist(playlist_id=playlist_id)
        created_playlist = sp.user_playlist_create(IMPORT_USERNAME, playlist['name'])
        playlist_map.append((playlist_id, created_playlist['id']))


def add_tracks_to_playlist(from_id, to_id):
    tracks = sp.playlist_tracks(from_id)
    while True:
        uri_list = list()
        for track in tracks['items']:
            uri_list.append(track['track']['uri'])
        sp.user_playlist_add_tracks(
            user=IMPORT_USERNAME,
            playlist_id=to_id,
            tracks=uri_list
        )
        if not tracks['next']:
            break
        tracks = sp.next(tracks)


def put_playlist_cover_image(from_id, to_id):
    image_url = sp.playlist_cover_image(from_id)
    image = requests.get(image_url[0]['url']).content
    if len(image) > 256000:
        return
    base64_cover = base64.b64encode(image).decode("utf-8")
    sp.playlist_upload_cover_image(to_id, base64_cover)


for from_id, to_id in playlist_map:
    add_tracks_to_playlist(from_id, to_id)

for from_id, to_id in playlist_map:
    put_playlist_cover_image(from_id, to_id)
