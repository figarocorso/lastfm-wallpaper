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
        self.image_updater = ImageUpdater('blue_eyes.jpg')

    def test_open_unexisting_image(self):
        self.assertRaises(IOError,self.image_updater.open_image,'notexisting.foo')

    def test_overlay_text(self):
        self.image_updater.set_font_properties()
        self.text = self.image_updater.create_text_image('Hello!', rotation = 10)
        self.base = self.image_updater.add_text_image(self.text)
        self.base.show()

    def tearDown(self):
        pass

if __name__ == "__main__":
    print "An image with a yellow 'hello!' should appear"
    unittest.main()
