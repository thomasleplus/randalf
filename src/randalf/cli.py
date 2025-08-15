"""Randalf CLI - Random String Generator CLI
Generates a random string of a specified length using a given alphabet or ASCII ranges.
"""

from typing import Optional

import typer
from rich.console import Console
from typing_extensions import Annotated

from . import __version__
from .core import alphabet_to_string, ranges_to_string

_err_console = Console(stderr=True)


def _version_callback(value: bool):
    """Prints version information and exits."""
    if value:
        typer.secho(f"randalf {__version__}")
        raise typer.Exit()


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


app = typer.Typer(context_settings={"help_option_names": ["-h", "--help"]})
app.command()(main)


if __name__ == "__main__":
    app()
