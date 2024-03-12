#!/usr/bin/env python
# -*- coding: utf-8 -*-
import subprocess
import sys
import click
from dugite.cli.commands import root


def is_pyenv_installed():
    try:
        subprocess.run(["pyenv", "--version"], capture_output=True, check=True)
        return True
    except FileNotFoundError:
        return False


def is_tfenv_installed():
    try:
        subprocess.run(["tfenv", "--version"], capture_output=True, check=True)
        return True
    except FileNotFoundError:
        return False


def main():
    if not is_pyenv_installed():
        click.echo("""
Pyenv is not installed. Please install Pyenv before using Dugite:
https://github.com/pyenv/pyenv?tab=readme-ov-file#installation""")
        sys.exit(1)

    if not is_tfenv_installed():
        click.echo("""
TFenv is not installed. Please install TFenv before using Dugite:
https://github.com/tfutils/tfenv?tab=readme-ov-file#installation""")
        sys.exit(1)
    root()


if __name__ == "__main__":
    main()
