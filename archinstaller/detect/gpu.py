"""
GPU detection.
"""

import shlex

from ..models import GPU
from ..models.enums import Vendor
from ..shell import capture


def _get_lspci() -> str:
    """Return machine-readable PCI device information."""

    return capture("lspci", "-mm")


def _parse_gpus(text: str) -> list[GPU]:
    """Parse lspci output and return detected GPUs."""

    gpus: list[GPU] = []

    for line in text.splitlines():
        fields = shlex.split(line)

        if len(fields) < 4:
            continue

        device_class = fields[1]

        if device_class not in (
            "VGA compatible controller",
            "3D controller",
            "Display controller",
        ):
            continue

        vendor_text = fields[2]
        model = fields[3]

        if "AMD" in vendor_text or "ATI" in vendor_text:
            vendor = Vendor.AMD
        elif "NVIDIA" in vendor_text:
            vendor = Vendor.NVIDIA
        elif "Intel" in vendor_text:
            vendor = Vendor.INTEL
        else:
            continue

        gpus.append(
            GPU(
                vendor=vendor,
                model=model,
            )
        )

    return gpus


def detect_gpus() -> list[GPU]:
    """Detect GPUs installed in the system."""

    return _parse_gpus(_get_lspci())
