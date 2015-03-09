import unittest
from snakeoil import TransmissionDaemon
from snakeoil import Torrent

class TestTorrent(unittest.TestCase):

    def setUp(self):
        self.torrent = 'http://sample-file.bazadanni.com/download/applications/torrent/sample.torrent'
        self.testurl = 'http://testurl'
        self.torrent_name = 'sample-file'

    def test_init(self):
        torrent = Torrent(self.torrent)
        self.assertEqual(torrent.location, self.torrent)

    def test_location(self):
        torrent = Torrent(self.torrent)
        torrent.location = self.testurl
        self.assertEqual(torrent.location, self.testurl)
        
    def test_name(self):
        torrent = Torrent(self.torrent)
        torrent.name = self.torrent_name
        self.assertEqual(self.torrent_name, torrent.name)


if __name__ == '__main__':
    unittest.main()
