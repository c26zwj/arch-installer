import unittest
from pathlib import Path

from archinstaller.detect.gpu import _parse_gpus
from archinstaller.models.enums import Vendor


DATA_DIR = Path(__file__).parent / "data"


class TestGPU(unittest.TestCase):
    def test_amd_gpus(self) -> None:
        text = (DATA_DIR / "amd_gpu.txt").read_text()

        gpus = _parse_gpus(text)

        self.assertEqual(len(gpus), 2)
        self.assertEqual(gpus[0].vendor, Vendor.AMD)
        self.assertEqual(
            gpus[0].model,
            "Navi 48 [Radeon RX 9070/9070 XT/9070 GRE]",
        )
        self.assertEqual(gpus[1].vendor, Vendor.AMD)
        self.assertEqual(gpus[1].model, "Raphael")

    def test_intel_gpu(self) -> None:
        text = (DATA_DIR / "intel_gpu.txt").read_text()

        gpus = _parse_gpus(text)

        self.assertEqual(len(gpus), 1)
        self.assertEqual(gpus[0].vendor, Vendor.INTEL)
        self.assertEqual(gpus[0].model, "Arc B580")

    def test_nvidia_gpu(self) -> None:
        text = (DATA_DIR / "nvidia_gpu.txt").read_text()

        gpus = _parse_gpus(text)

        self.assertEqual(len(gpus), 1)
        self.assertEqual(gpus[0].vendor, Vendor.NVIDIA)
        self.assertEqual(gpus[0].model, "GeForce RTX 5080")


if __name__ == "__main__":
    unittest.main()
