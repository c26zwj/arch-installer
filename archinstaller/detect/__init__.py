"""
    detect package
"""

from .cpu import detect_cpu
from .disks import detect_disks
from .memory import detect_memory
from .gpu import detect_gpus

__all__ = [
    "detect_cpu",
    "detect_disks",
    "detect_gpus",
    "detect_memory",
]
