"""
Disk detection.
"""

import json
import subprocess
from pathlib import Path

from ..models import Disk


def detect_disks() -> list[Disk]:
    """
    Return all physical disks.
    """

    result = subprocess.run(
        [
            "lsblk",
            "--json",
            "--output",
            "NAME,PATH,SIZE,TYPE,TRAN,MODEL,VENDOR,SERIAL,RM,HOTPLUG",
        ],
        check=True,
        capture_output=True,
        text=True,
    )

    data = json.loads(result.stdout)

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
