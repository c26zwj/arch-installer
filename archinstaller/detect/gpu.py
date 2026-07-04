from ..models import GPU
from ..shell import capture


def _get_lspci() -> str:
    return capture("lspci", "-mm")


def _parse_gpu(text: str) -> GPU:
    """
    Parse lspci output and return the primary GPU.
    """
    ...


def detect_gpu() -> GPU:
    return _parse_gpu(_get_lspci())
