from spotify_actions import export_actions


class Export:
    def __init__(self, sp, username):
        self.sp = sp
        self.library = dict()
        self.username = username

    def export(self):
        self.library['followed_artists'] = self.get_followed_artists()
        self.library['ordered_playlists'], self.library['followed_playlists'] = self.get_playlists()
        self.library['saved_songs'] = self.get_saved_songs()
        self.library['saved_albums'] = self.get_albums()
        return self.library

    def get_albums(self):
        album_exporter = export_actions.ExportAlbums(self.sp, 'exporting albums')
        album_exporter.run()
        return album_exporter.library

    def get_saved_songs(self):
        song_exporter = export_actions.ExportSavedSongs(self.sp, 'exporting songs')
        song_exporter.run()
        return song_exporter.library

    def get_followed_artists(self):
        followed_artists_exporter = export_actions.ExportFollowedArtists(self.sp, 'exporting followed artists')
        followed_artists_exporter.run()
        return followed_artists_exporter.library

    def get_playlists(self):
        playlist_exporter = export_actions.ExportPlaylists(self.sp, 'exporting playlists', self.username)
        playlist_exporter.run()
        return playlist_exporter.library, playlist_exporter.followed_playlists
