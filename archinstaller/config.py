"""
Configuration classes and enums for the installer.
"""

from dataclasses import dataclass, field
from .models import CPU, Disk, GPU
from enum import Enum, auto
from pathlib import Path

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


@dataclass
class Config:
    """Installer configuration."""

    # System
    hostname: str = "Charles-PC"
    username: str = "charles"

    timezone: str = "America/New_York"
    locale: str = "en_US.UTF-8"

    # Installation
    bootloader: Bootloader = Bootloader.GRUB
    filesystem: Filesystem = Filesystem.BTRFS
    desktop: Desktop = Desktop.KDE

    # Hardware (detected later)
    cpu: CPU | None = None
    gpu: GPU | None = None
    disks: list[Disk] = field(default_factory=list)

    ram_gib: int = 0

    disk: Path | None = None

    # Memory
    swap_gib: int = 0
    zram_gib: int = 0

    # Applications
    install_steam: bool = True
    install_vivaldi: bool = True
    install_obsidian: bool = True
    install_pycharm: bool = True
    install_zed: bool = True
    install_vorta: bool = True
    install_scrcpy: bool = True
