#!/usr/bin/env python3

from installer.config import Config
from installer.detect import detect_memory


def main() -> None:

    cfg = Config()
    cfg.ram_gib = detect_memory()

    print("Arch Installer v0.1.0")
    print()

    print(f"{'Hostname':<12}: {cfg.hostname}")
    print(f"{'Username':<12}: {cfg.username}")
    print(f"{'Timezone':<12}: {cfg.timezone}")
    print(f"{'Filesystem':<12}: {cfg.filesystem.name}")
    print(f"{'Desktop':<12}: {cfg.desktop.name}")
    print(f"{'Bootloader':<12}: {cfg.bootloader.name}")

    print(f"{'Memory':<12}: {cfg.ram_gib} GiB")

if __name__ == "__main__":
    main()
