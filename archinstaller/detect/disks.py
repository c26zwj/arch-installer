"""
Disk detection.
"""

import json
from pathlib import Path

from ..models import Disk
from ..shell import capture


def detect_disks() -> list[Disk]:
    """
    Return all physical disks.
    """

    text = capture(
        "lsblk",
        "--json",
        "--output",
        "NAME,PATH,SIZE,TYPE,TRAN,MODEL,VENDOR,SERIAL,RM,HOTPLUG",
    )

    data = json.loads(text)

    disks: list[Disk] = []
    for device in data["blockdevices"]:
        if device["type"] != "disk":
            continue

        path = Path(device["path"])

        ignored_prefixes = ("zram", "loop", "dm-")
        if path.name.startswith(ignored_prefixes):
            continue

        disks.append(
            Disk(
                path=path,
                name=device["name"],
                model=(device.get("model") or "").strip(),
                vendor=(device.get("vendor") or "").strip(),
                serial=(device.get("serial") or "").strip(),
                size=device["size"],
                transport=device.get("tran") or "",
                removable=bool(device["rm"]),
                hotplug=bool(device["hotplug"]),
            )
        )

    return disks
