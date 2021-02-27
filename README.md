# Spotify Move
Scripts to move library from one Spotify account to another account.

## Instalation
You can install needed packages using the following command.
```
pip install -r requirements.txt
```

## Running
For running this scripts first you need to create a developer app in [Spotify developer dashboard](https://developer.spotify.com/dashboard/).  
After that you need to go to settings of the app that you created and put a url in `Redirect URLs`. I put `http://localhost`. If you use someother URL you need to change `redirect_uri` in `import.py` and `export.py` file.  
After that you need to craete an environment file in base folder named `.env` with these arguments in it.
```
CLIENT_ID='your-spotify-developer-app-client-id'
CLIENT_SECRET='your-spotify-developer-app-client-secret'
EXPORT_USERNAME='spotify-id-of-account-you-are-exporting-from'
IMPORT_USERNAME='spotify-id-of-account-you-are-importing-to'
```
After that you you can run `export.py` that creates a json file that has spotify ids of all the playlists and artists that you followed, songs saved in liked songs, albums saved, playlists created.  
After that you can run `import.py` that reads the json files created and follows artists and playlists, likes albums, creates playlists and likes songs. It saves the arrangement of liked songs and your playlists and the songs inside the playlists. 

## TODO
  - refactor my codes
  - see if there is a better way to move liked songs (its slow right now)
  - move playlist cover images
  - use a progress bar each step
