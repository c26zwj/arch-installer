#!/usr/bin/env python3

from . import PROJECT_NAME, VERSION
from .config import Config
from .detect import (
    detect_cpu,
    detect_disks,
    detect_firmware,
    detect_gpus,
    detect_memory,
    detect_network,
)

def main() -> None:
    cfg = Config()

    cfg.firmware = detect_firmware()
    cfg.ram_gib = detect_memory()
    cfg.cpu = detect_cpu()
    cfg.gpus = detect_gpus()
    cfg.disks = detect_disks()

    print(f"{PROJECT_NAME} v{VERSION}")
    print()

    print(f"{'Firmware':<12}: {'UEFI' if cfg.firmware.uefi else 'BIOS'}")
    print(f"{'Secure Boot':<12}: {'Enabled' if cfg.firmware.secure_boot else 'Disabled'}")

    print(f"{'Hostname':<12}: {cfg.hostname}")
    print(f"{'Username':<12}: {cfg.username}")
    print(f"{'Timezone':<12}: {cfg.timezone}")
    print(f"{'Filesystem':<12}: {cfg.filesystem.name}")
    print(f"{'Desktop':<12}: {cfg.desktop.name}")
    print(f"{'Bootloader':<12}: {cfg.bootloader.name}")
    print()

    print(f"{'Memory':<12}: {cfg.ram_gib} GiB")
    print()

    print(f"{'CPU':<12}: {cfg.cpu.model}")
    print(f"{'Vendor':<12}: {cfg.cpu.vendor.name}")
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

    print()
    print("GPUs")
    print("-" * 60)

    for gpu in cfg.gpus:
        print(f"{gpu.vendor.name:<8} {gpu.model}")
    print()

    cfg.online = detect_network()
    print(
        f"{'Internet':<12}: "
        f"{'Connected' if cfg.online else 'Offline'}"
    )
