import unittest
from LastFm import *
from BackgroundManager import *
from ImageUpdater import *

class LastFmTest(unittest.TestCase):

    def setUp(self):
        self.my_lastfm = LastFm('figarocorso')

    def testConection(self):
       self.assertEqual('figarocorso', self.my_lastfm.get_username())

    def tearDown(self):
        pass

class BackgroundManagerTest(unittest.TestCase):

    def setUp(self):
        self.background_manager = BackgroundManager()

    def testGetWallpaper(self):
        self.assertIn('file://',self.background_manager.getWallpaperUri())

    def tearDown(self):
        pass

class ImageUpdaterTest(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()
