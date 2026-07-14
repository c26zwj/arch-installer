"""
CPU detection.
"""

from pathlib import Path

from archinstaller.models.enums import Vendor

from ..models import CPU


def detect_cpu() -> CPU:
    """
    Detect the installed CPU.
    """

    vendor = None
    model = ""
    microcode = ""

    for line in Path("/proc/cpuinfo").read_text().splitlines():
        if line.startswith("vendor_id"):
            if line.find("AuthenticAMD") != -1:
                vendor = Vendor.AMD
                microcode = "amd-ucode"
            elif line.find("GenuineIntel") != -1:
                vendor = Vendor.INTEL
                microcode = "intel-ucode"
        elif line.startswith("model name"):
            model = line.split(":", 1)[1].strip()

        if vendor and model:
            break

    return CPU(
        vendor=vendor,
        model=model,
        microcode=microcode,
    )
