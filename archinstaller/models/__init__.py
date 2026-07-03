"""
    modules init
"""

from .cpu import CPU
from .disk import Disk
from .gpu import GPU

__all__ = [
    "CPU",
    "GPU",
    "Disk",
]
