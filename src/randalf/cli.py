"""Randalf CLI - Random String Generator CLI
Generates a random string of a specified length using a given alphabet or ASCII ranges.
"""

import typer

from .randalf import main

app = typer.Typer(context_settings={"help_option_names": ["-h", "--help"]})
app.command()(main)

if __name__ == "__main__":
    app()
