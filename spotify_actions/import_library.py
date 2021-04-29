from spotify_actions import import_actions


class Import:
    def __init__(self, sp, username, library):
        self.sp = sp
        self.username = username
        self.library = library

    def import_library(self):
        self.import_albums()
        self.import_songs()
        self.import_playlists()
        self.import_followed_artists()

    def import_albums(self):
        albums_list = self.library['saved_albums']
        album_importer = import_actions.ImportAlbum(self.sp, albums_list, 'importing albums')
        album_importer.run()

    def import_songs(self):
        songs_list = self.library['saved_songs']
        songs_importer = import_actions.ImportSavedTracks(self.sp, songs_list, 'importing songs')
        songs_importer.run()

    def import_followed_artists(self):
        artist_list = self.library['followed_artists']
        artist_importer = import_actions.ImportFollowedArtists(self.sp, artist_list, 'importing followed artists')
        artist_importer.run()

    def import_playlists(self):
        playlist_list = self.library['ordered_playlists']
        followed_playlists = self.library['followed_playlists']
        playlist_importer = import_actions.ImportPlayLists(
            self.sp,
            playlist_list,
            'importing playlists',
            self.username,
            followed_playlists
        )
        playlist_importer.run()
