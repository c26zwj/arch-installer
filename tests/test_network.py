import unittest
from unittest.mock import patch

from archinstaller.detect.network import detect_network


class TestNetwork(unittest.TestCase):
    @patch("archinstaller.detect.network.socket.create_connection")
    def test_network_connected(self, mock_connection) -> None:
        mock_connection.return_value.__enter__.return_value = None

        self.assertTrue(detect_network())

    @patch("archinstaller.detect.network.socket.create_connection")
    def test_network_offline(self, mock_connection) -> None:
        mock_connection.side_effect = OSError

        self.assertFalse(detect_network())


if __name__ == "__main__":
    unittest.main()
