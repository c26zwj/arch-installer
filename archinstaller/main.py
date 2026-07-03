#!/usr/bin/env python3

from . import PROJECT_NAME, VERSION
from .config import Config
from .detect import detect_cpu, detect_memory, detect_disks


def main() -> None:


    cfg = Config()
    cfg.ram_gib = detect_memory()
    cfg.cpu = detect_cpu()
    cfg.disks = detect_disks()

    print(f"{PROJECT_NAME} v{VERSION}")
    print()

    print(f"{'Hostname':<12}: {cfg.hostname}")
    print(f"{'Username':<12}: {cfg.username}")
    print(f"{'Timezone':<12}: {cfg.timezone}")
    print(f"{'Filesystem':<12}: {cfg.filesystem.name}")
    print(f"{'Desktop':<12}: {cfg.desktop.name}")
    print(f"{'Bootloader':<12}: {cfg.bootloader.name}")

    print(f"{'Memory':<12}: {cfg.ram_gib} GiB")
    print()

    print(f"{'CPU':<12}: {cfg.cpu.model}")
    print(f"{'Vendor':<12}: {cfg.cpu.vendor}")
    print(f"{'Microcode':<12}: {cfg.cpu.microcode}")
    print()

    print("Disks")
    print("-" * 60)

    for disk in cfg.disks:
        print(
            f"{disk.path} "
            f"{disk.size:<8} "
            f"{disk.transport:<5} "
            f"{disk.model}"
        )
