from gi.repository import Gio

class BackgroundManager():
    SCHEMA = 'org.gnome.desktop.background'
    KEY = 'picture-uri'

    def __init__(self):
        self.gsettings = Gio.Settings.new(self.SCHEMA)

    def getWallpaperUri(self):
        return self.gsettings.get_string(self.KEY)

    def setWallpaperUri(self, new_wallpaper):
        self.gsettings.set_string(self.KEY, new_wallpaper)
        self.gsettings.apply()
