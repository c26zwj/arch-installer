"""
Memory detection.
"""

from pathlib import Path


def detect_memory() -> int:
    """
    Return installed RAM in GiB.
    """

    meminfo = Path("/proc/meminfo").read_text()

    for line in meminfo.splitlines():
        if line.startswith("MemTotal:"):
            kib = int(line.split()[1])
            gib = kib / 1024 / 1024

            # Round to common RAM sizes
            for size in (4, 8, 16, 24, 32, 48, 64, 96, 128, 192, 256):
                if abs(gib - size) < 2:
                    return size

            return round(gib)

    raise RuntimeError("Unable to detect system memory.")
