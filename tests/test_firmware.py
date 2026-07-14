import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from archinstaller.detect.firmware import _detect_secure_boot


class TestFirmware(unittest.TestCase):
    def test_secure_boot_enabled(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            efivars = Path(temp_dir)
            secure_boot = efivars / "SecureBoot-test"

            secure_boot.write_bytes(bytes([6, 0, 0, 0, 1]))

            with patch(
                "archinstaller.detect.firmware.EFIVARS_PATH",
                efivars,
            ):
                self.assertTrue(_detect_secure_boot())

    def test_secure_boot_disabled(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            efivars = Path(temp_dir)
            secure_boot = efivars / "SecureBoot-test"

            secure_boot.write_bytes(bytes([6, 0, 0, 0, 0]))

            with patch(
                "archinstaller.detect.firmware.EFIVARS_PATH",
                efivars,
            ):
                self.assertFalse(_detect_secure_boot())


if __name__ == "__main__":
    unittest.main()
