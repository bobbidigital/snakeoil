import unittest
from snakeoil import TransmissionDaemon
from snakeoil import Torrent

class  TestTransmission(unittest.TestCase):

    def setUp(self):
        self.torrent = 'http://sample-file.bazadanni.com/download/applications/torrent/sample.torrent'
        self.port = '9091'
        self.host = '192.168.1.12'
        self.SUCCESS = 'success'

    def test_init(self):
        daemon = TransmissionDaemon(host=self.host)
        self.assertEqual(daemon.host, self.host)
        self.assertEqual(daemon.port, self.port)

    def test_add_torrent(self):
        daemon = TransmissionDaemon(host=self.host)
        torrent = Torrent(self.torrent)
        response = daemon.add_torrent(torrent)
        self.assertEqual(response['result'], self.SUCCESS)




if __name__ == '__main__':
    unittest.main()
