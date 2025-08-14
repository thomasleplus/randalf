"""Randalf - Random String Generator
Generates a random string of a specified length using a given alphabet or ASCII ranges.
"""

import random
import re
from typing import Optional

import typer
from rich.console import Console
from typing_extensions import Annotated

__all__ = [
    "alphabet_to_string",
    "list_to_string",
    "main",
    "ranges_to_string",
]
__version__ = "1.0.0"
_err_console = Console(stderr=True)


def _alphabet_to_list(alphabet: str) -> list:
    """Converts an ASCII string into a character list."""
    return sorted(set(alphabet))


def _ranges_to_list(pattern: str) -> list:
    """Converts an ASCII range like '0-9A-F' into a character list."""
    chars = []
    regex = re.compile(f"^[{pattern}]$")
    for i in range(256):
        c = chr(i)
        if regex.match(c):
            chars.append(c)
    return chars


def _version_callback(value: bool):
    """Prints version information and exits."""
    if value:
        typer.secho(f"randalf {__version__}")
        raise typer.Exit()


def list_to_string(alphabet: list, length: int) -> str:
    """Generates a random string of given length from the provided list of characters."""
    return "".join(random.choice(alphabet) for _ in range(length))


def alphabet_to_string(alphabet: str, length: int) -> str:
    """Generates a random string of given length from the characters in the provided string."""
    return list_to_string(_alphabet_to_list(alphabet), length)


def ranges_to_string(ranges: str, length: int) -> str:
    """Generates a random string of given length from the character ranges provided."""
    return list_to_string(_ranges_to_list(ranges), length)


def main(
    length: Annotated[
        int,
        typer.Option("--length", "-l", help="Choose the length of the output string."),
    ],
    alphabet: Annotated[
        Optional[str],
        typer.Option(
            "--alphabet",
            "-a",
            help="Choose the alphabet using an ASCII string, e.g. '0123456789abcdef'.",
        ),
    ] = None,
    ranges: Annotated[
        Optional[str],
        typer.Option(
            "--ranges",
            "-r",
            help="Choose the alphabet using ASCII ranges, e.g. 'a-z0-9', '\\w' or '^\\x00-\\x1f'.",
        ),
    ] = None,
    # pylint: disable-next=unused-argument
    version: Annotated[
        Optional[bool],
        typer.Option(
            "--version",
            "-v",
            help="Show version and exit.",
            callback=_version_callback,
            is_eager=True,
        ),
    ] = None,
):
    """
    Conjure a random string of desired length using chosen alphabet.
    """

    if length < 0:
        _err_console.print("error: length must be positive.")
        raise typer.Exit(code=1)

    if length == 0:
        raise typer.Exit()

    if alphabet and ranges:
        _err_console.print(
            "error: conflicting options: specify --alphabet or --ranges."
        )
        raise typer.Exit(code=1)

    if alphabet:
        print(alphabet_to_string(alphabet, length))
    elif ranges:
        print(ranges_to_string(ranges, length))
    else:
        _err_console.print("error: missing option: specify --alphabet or --ranges.")
        raise typer.Exit(code=1)
