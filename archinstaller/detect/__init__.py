"""
    detect package
"""

from .cpu import detect_cpu
from .disks import detect_disks
from .memory import detect_memory
from .gpu import detect_gpus
from .firmware import detect_firmware

__all__ = [
    "detect_cpu",
    "detect_disks",
    "detect_firmware",
    "detect_gpus",
    "detect_memory",
]
