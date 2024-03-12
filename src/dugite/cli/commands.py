#!/usr/bin/env python
# -*- coding: utf-8 -*-
import click
import sys
from dugite.skeleton.builder import create_project_structure
from dugite.template.builder import initialize_files
from dugite.controllers.builder import generate_controller
from dugite.dependencies.checker import is_pyenv_installed, is_tfenv_installed


@click.group()
def root():
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


@click.command(name="new", help="Create a new project.")
@click.argument('name')
@click.option('--python-version', default="3.12",
              help='Python version of the Lambda Functions.')
@click.option('--terraform-version', default="1.7",
              help='Python version of the Lambda Functions.')
def initializer(name, python_version, terraform_version):
    create_project_structure(name)
    initialize_files(name, python_version, terraform_version)


@click.group(name="g", help="Generate project components.")
def generator():
    pass


@click.command(name="controller", help="Generate a controller.")
@click.argument('name')
def controller_generator(name):
    generate_controller(name)


@click.command(name="model", help="Generate a model.")
@click.argument('name')
def model_generator(name):
    click.echo('Generate model')


root.add_command(initializer)
root.add_command(generator)
generator.add_command(controller_generator)
generator.add_command(model_generator)
