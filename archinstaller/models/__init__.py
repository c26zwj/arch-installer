"""
    modules init
"""

from .cpu import CPU
from .disk import Disk
from .gpu import GPU
from .firmware import Firmware


__all__ = [
    "CPU",
    "Disk",
    "Firmware",
    "GPU",
]
