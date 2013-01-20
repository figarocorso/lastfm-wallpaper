import urlparse
from LastFm import *
from BackgroundManager import *
from ImageUpdater import *

class LastFmWallpaperUpdater():

    def __init__(self, username):
        self.username = username
        self.wallpaper_path = ''
        self.total_scrobblings = None
        self.week_artists = None
        self.modified_image = None
        self.new_image_path = ""

    def update_wallpaper(self):
        if not self.wallpaper_path:
            self.obtain_wallpaper_path()

        self.obtain_lastfm_data()
        self.generate_new_image()
        self.generate_new_image_path()
        self.modified_image.save(self.new_image_path,'JPEG')
        self.set_new_wallpaper()

    def obtain_wallpaper_path(self):
        self.background_manager = BackgroundManager()
        self.wallpaper_uri = self.background_manager.getWallpaperUri()
        self.wallpaper_path = urlparse.urlparse(self.wallpaper_uri).path

    def set_new_wallpaper(self):
        self.background_manager = BackgroundManager()
        self.wallpaper_uri = self.background_manager.setWallpaperUri('file://' + self.new_image_path)

    def obtain_lastfm_data(self):
        self.my_lastfm = LastFm(self.username)
        self.total_scrobblings = self.my_lastfm.get_number_scrobblings()
        self.week_artists = self.my_lastfm.get_week_artist(3)

    def generate_new_image(self):
        print 'Base image: ' + self.wallpaper_path
        self.image_updater = ImageUpdater(self.wallpaper_path)
        self.image_updater.add_username(self.username)
        self.image_updater.add_scrobblings(self.total_scrobblings)
        self.image_updater.weekly_chart(self.week_artists)
        self.modified_image = self.image_updater.get_base_image()

    def generate_new_image_path(self):
        self.new_image_path = self.wallpaper_path[:(self.wallpaper_path.rfind('.')-1)]
        self.new_image_path += '$'
        self.new_image_path += self.wallpaper_path[self.wallpaper_path.rfind('.'):]

if __name__ == "__main__":
    LastFmWallpaperUpdater('figarocorso').update_wallpaper()
