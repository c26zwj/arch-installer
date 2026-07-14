"""
Configuration classes and enums for the installer.
"""

from dataclasses import dataclass, field

from .models import CPU, Disk, Firmware, GPU
from .models.enums import Bootloader, Desktop, Filesystem


@dataclass(slots=True)
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
    firmware: Firmware | None = None
    cpu: CPU | None = None
    gpus: list[GPU] = field(default_factory=list)
    disks: list[Disk] = field(default_factory=list)
    ram_gib: int = 0
    online: bool = False

    selected_disk: Disk | None = None

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
