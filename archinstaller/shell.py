"""
Shell command helpers.
"""

from subprocess import run


def capture(*command: str) -> str:
    """
    Run a command and return stdout.

    Raises:
        subprocess.CalledProcessError
            If the command exits with a non-zero status.
    """
    result = run(
        command,
        check=True,
        capture_output=True,
        text=True,
    )

    return result.stdout
