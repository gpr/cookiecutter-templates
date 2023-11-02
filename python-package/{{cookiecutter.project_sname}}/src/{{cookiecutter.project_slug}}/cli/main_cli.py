# -*- coding: utf-8 -*-
"""Main CLI module."""

import click

from {{cookiecutter.project_slug}} import __version__


@click.command()
@click.version_option(__version__)
def main_cli():
    """Entry point for the CLI."""
    print("Hello world!")


if __name__ == "__main__":
    main_cli()  # pragma: no cover
