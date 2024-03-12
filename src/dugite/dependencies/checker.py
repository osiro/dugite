#!/usr/bin/env python
# -*- coding: utf-8 -
import subprocess


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
