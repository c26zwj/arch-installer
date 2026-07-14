from dataclasses import dataclass

from .enums import Vendor


@dataclass(slots=True)
class CPU:
    """Information about the installed CPU."""

    vendor: Vendor
    model: str
    microcode: str
