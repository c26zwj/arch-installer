from dataclasses import dataclass
from pathlib import Path


@dataclass(slots=True)
class Disk:
    """Physical storage device."""

    path: Path
    name: str
    model: str
    vendor: str
    serial: str
    size: str
    transport: str
    removable: bool
    hotplug: bool

    @property
    def is_nvme(self) -> bool:
        return self.transport == "nvme"

    @property
    def is_usb(self) -> bool:
        return self.transport == "usb"

    @property
    def is_internal(self) -> bool:
        return not self.removable and not self.hotplug

    @property
    def display_name(self) -> str:
        if self.vendor:
            return f"{self.vendor} {self.model}".strip()
        return self.model
