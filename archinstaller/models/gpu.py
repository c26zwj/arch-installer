from dataclasses import dataclass

from .enums import Vendor


@dataclass(slots=True)
class GPU:
    vendor: Vendor
    model: str
