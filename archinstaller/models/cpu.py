from dataclasses import dataclass


@dataclass(slots=True)
class CPU:
    """Information about the installed CPU."""

    vendor: str
    model: str
    microcode: str
