from spotify_actions.abstract_export import ExportAction


class ExportAlbums(ExportAction):
    def get_first_batch(self):
        self.batch = self.sp.current_user_saved_albums()

    def do_action(self):
        self.make_progress_bar(self.batch['total'], self.title)
        while True:
            for album in self.batch['items']:
                self.library.append(album['album']['id'])
                self.update_progress_bar(1)
            if not self.batch['next']:
                break
            self.get_next_batch()
        self.pb.close()


class ExportSavedSongs(ExportAction):
    def get_first_batch(self):
        self.batch = self.sp.current_user_saved_tracks()

    def do_action(self):
        self.make_progress_bar(self.batch['total'], self.title)
        while True:
            for track in self.batch['items']:
                self.library.append(track['track']['id'])
                self.update_progress_bar(1)
            if not self.batch['next']:
                break
            self.get_next_batch()
        self.pb.close()


class ExportFollowedArtists(ExportAction):
    def get_first_batch(self):
        self.batch = self.sp.current_user_followed_artists()['artists']

    def get_next_batch(self):
        self.batch = self.sp.next(self.batch)['artists']

    def do_action(self):
        self.make_progress_bar(self.batch['total'], self.title)
        while True:
            followed_artists = self.batch
            for artist in followed_artists['items']:
                self.library.append(artist['id'])
                self.update_progress_bar(1)
            if not followed_artists['next']:
                break
            self.get_next_batch()
        self.pb.close()


class ExportPlaylists(ExportAction):
    def __init__(self, sp, title, username):
        super().__init__(sp, title)
        self.followed_playlists = list()
        self.username = username

    def get_first_batch(self):
        self.batch = self.sp.current_user_playlists()

    def do_action(self):
        self.make_progress_bar(self.batch['total'], self.title)
        while True:
            for playlist in self.batch['items']:
                self.library.append(playlist['id'])
                self.update_progress_bar(1)
                if playlist['owner']['id'] != self.username:
                    self.followed_playlists.append(playlist['id'])
            if not self.batch['next']:
                break
            self.get_next_batch()
        self.pb.close()
