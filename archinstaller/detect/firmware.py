"""
Firmware detection.
"""

from pathlib import Path

from ..models import Firmware


EFI_PATH = Path("/sys/firmware/efi")
EFIVARS_PATH = EFI_PATH / "efivars"

SECURE_BOOT_PREFIX = "SecureBoot-"


def _detect_secure_boot() -> bool:
    """Return whether UEFI Secure Boot is enabled."""

    if not EFIVARS_PATH.exists():
        return False

    secure_boot_vars = list(
        EFIVARS_PATH.glob(f"{SECURE_BOOT_PREFIX}*")
    )

    if not secure_boot_vars:
        return False

    data = secure_boot_vars[0].read_bytes()

    if len(data) < 5:
        raise RuntimeError(
            "Secure Boot EFI variable contains invalid data."
        )

    return data[4] == 1


def detect_firmware() -> Firmware:
    """Detect firmware boot mode and Secure Boot state."""

    uefi = EFI_PATH.exists()

    return Firmware(
        uefi=uefi,
        secure_boot=_detect_secure_boot() if uefi else False,
    )
