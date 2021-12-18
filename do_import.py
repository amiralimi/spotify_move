from spotify_actions.import_library import Import

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
REDIRECT_URI = os.getenv('REDIRECT_URI')


def import_():
    sp = spotipy.Spotify(
        auth_manager=SpotifyOAuth(
            scope=scope,
            client_id=CLIENT_ID,
            client_secret=CLIENT_SECRET,
            username=IMPORT_USERNAME,
            redirect_uri=REDIRECT_URI
        )
    )
    with open('exported_data.json', 'r') as jf:
        library = json.load(jf)
    importer = Import(sp, IMPORT_USERNAME, library)
    importer.import_library()
