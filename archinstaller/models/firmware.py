from dataclasses import dataclass


@dataclass(slots=True)
class Firmware:
    """Detected system firmware information."""

    uefi: bool
    secure_boot: bool
