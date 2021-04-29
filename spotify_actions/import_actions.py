import time
from spotify_actions.abstract_import import ImportAction


class ImportAlbum(ImportAction):
    def do_action(self):
        total = len(self.items)
        for i in range(0, total, 50):
            batch = self.items[i:min(i + 50, total)]
            self.sp.current_user_saved_albums_add(albums=batch)
            self.update_progress_bar(50)


class ImportFollowedArtists(ImportAction):
    def do_action(self):
        total = len(self.items)
        for i in range(0, total, 50):
            batch = self.items[i: min(i + 50, total)]
            self.sp.user_follow_artists(ids=batch)
            self.update_progress_bar(50)


class ImportSavedTracks(ImportAction):
    def do_action(self):
        self.items.reverse()
        for track_id in self.items:
            self.sp.current_user_saved_tracks_add(tracks=[track_id])
            time.sleep(0.4)
            self.update_progress_bar(1)


class ImportPlayLists(ImportAction):
    def __init__(self, sp, items, title, username, followed_playlists):
        super().__init__(sp, items, title)
        self.username = username
        self.followed_playlists = followed_playlists
        self.playlist_map = list()

    def do_action(self):
        self.items.reverse()
        for playlist_id in self.items:
            if playlist_id in self.followed_playlists:
                self.sp.current_user_follow_playlist(playlist_id=playlist_id)
            else:
                playlist = self.sp.playlist(playlist_id=playlist_id)
                created_playlist = self.sp.user_playlist_create(self.username, playlist['name'])
                self.playlist_map.append((playlist_id, created_playlist['id']))
            self.update_progress_bar(1)

        self.pb.close()
        self.make_progress_bar(len(self.playlist_map), 'making your playlists')
        for from_id, to_id in self.playlist_map:
            self.add_tracks_to_playlist(from_id, to_id)
            self.put_playlist_cover_image(from_id, to_id)
            self.update_progress_bar(1)

    def add_tracks_to_playlist(self, from_id, to_id):
        tracks = self.sp.playlist_tracks(from_id)
        while True:
            uri_list = list()
            for track in tracks['items']:
                uri_list.append(track['track']['uri'])
            self.sp.user_playlist_add_tracks(
                user=self.username,
                playlist_id=to_id,
                tracks=uri_list
            )
            if not tracks['next']:
                break
            tracks = self.sp.next(tracks)

    def put_playlist_cover_image(self, from_id, to_id):
        # image_url = self.sp.playlist_cover_image(from_id)
        pass
