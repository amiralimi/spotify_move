# Spotify Move
Scripts to move Spotify library from one account to another.

## Installation
You can install needed packages using the following command.
```
pip install -r requirements.txt
```

## Running
For running this scripts first you need to create a developer app in [Spotify developer dashboard](https://developer.spotify.com/dashboard/).  
After that you need to go to settings of the app that you created and put a url in `Redirect URLs`. I put `http://localhost`. If you use some other URL you need to change `redirect_uri` in `import.py` and `export.py` file.  
After that you need to create an environment file in base folder named `.env` with these arguments in it.
```
CLIENT_ID='your-spotify-developer-app-client-id'
CLIENT_SECRET='your-spotify-developer-app-client-secret'
EXPORT_USERNAME='spotify-id-of-account-you-are-exporting-from'
IMPORT_USERNAME='spotify-id-of-account-you-are-importing-to'
```
After that you you can run `move.py`. Its has `export` and `import_` functions in it. Running `export` makes a json file that represents your library. Running `import_` function reads the json file and adds the library to the other account. It saves the arrangement of liked songs and your playlists and the songs inside the playlists.  
First time running each function a browser will open so you could login with your account and in terminal you will be prompted to input the url that you are redirected to.

## TODO
  - See if there is a better way to move liked songs (its slow right now)
  - Move playlist cover images
  - Create a web server to automatically capture the link so its not needed to copy it manually into the terminal.
  - Add some cl arguments so the process is easily controllable. 
