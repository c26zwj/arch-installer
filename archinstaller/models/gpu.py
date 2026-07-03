from dataclasses import dataclass


@dataclass(slots=True)
class GPU:
    """Information about the installed GPU."""

    vendor: str
    model: str
    driver: str
