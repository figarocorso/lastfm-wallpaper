import unittest
from LastFm import *

class LastFmTest(unittest.TestCase):
    def setUp(self):
        self.my_lastfm = LastFm('figarocorso')

    def testConection(self):
       self.assertEqual('figarocorso', self.my_lastfm.get_username())

    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()
