import unittest

from archinstaller.detect.memory import detect_memory


class TestMemory(unittest.TestCase):
    def test_memory(self):
        self.assertGreaterEqual(detect_memory(), 1)
