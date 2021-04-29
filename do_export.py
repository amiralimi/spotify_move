import spotipy
import json
import os

from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyOAuth

from spotify_actions.export_library import Export

SCOPE = 'user-library-read playlist-read-private playlist-read-collaborative user-follow-read'

load_dotenv()
CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')
EXPORT_USERNAME = os.getenv('EXPORT_USERNAME')

REDIRECT_URI = 'http://localhost'


def export():
    sp = spotipy.Spotify(
        auth_manager=SpotifyOAuth(
            scope=SCOPE,
            client_id=CLIENT_ID,
            client_secret=CLIENT_SECRET,
            username=EXPORT_USERNAME,
            redirect_uri=REDIRECT_URI
        )
    )
    exporter = Export(sp, EXPORT_USERNAME)
    library = exporter.export()
    with open('exported_data.json', 'w') as jf:
        json.dump(library, jf)
