import unittest
import requests
from snakeoil import TransmissionDaemon
from snakeoil import Torrent
import mock


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

    @mock.patch.object(requests, 'post', autospec=True) 
    def test_add_torrent(self, mock_object):
        daemon = TransmissionDaemon(host=self.host)
        torrent = Torrent(self.torrent)
        response = daemon.add_torrent(torrent)
        assert mock_object.called




if __name__ == '__main__':
    unittest.main()
