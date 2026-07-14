from enum import Enum, auto


class Bootloader(Enum):
    """Supported bootloaders."""

    GRUB = auto()
    SYSTEMD_BOOT = auto()


class Filesystem(Enum):
    """Supported filesystems."""

    BTRFS = auto()
    EXT4 = auto()


class Desktop(Enum):
    """Supported desktop environments."""

    KDE = auto()
    GNOME = auto()
    XFCE = auto()
    NONE = auto()


class Vendor(Enum):
    """Supported GPU/CPU vendors."""

    INTEL = auto()
    AMD = auto()
    NVIDIA = auto()
