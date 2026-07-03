"""
CPU detection.
"""

from pathlib import Path

from ..models import CPU


def detect_cpu() -> CPU:
    """
    Detect the installed CPU.
    """

    vendor = ""
    model = ""

    for line in Path("/proc/cpuinfo").read_text().splitlines():

        if line.startswith("vendor_id"):
            vendor = line.split(":", 1)[1].strip()

        elif line.startswith("model name"):
            model = line.split(":", 1)[1].strip()

        if vendor and model:
            break

    match vendor:
        case "AuthenticAMD":
            vendor = "AMD"
            microcode = "amd-ucode"

        case "GenuineIntel":
            vendor = "Intel"
            microcode = "intel-ucode"

        case _:
            microcode = ""

    return CPU(
        vendor=vendor,
        model=model,
        microcode=microcode,
    )
