"""
Network connectivity detection.
"""

import socket


def detect_network() -> bool:
    """Return whether the system has Internet connectivity."""

    try:
        with socket.create_connection(
            ("archlinux.org", 443),
            timeout=3,
        ):
            return True
    except OSError:
        return False
