#!/usr/bin/env python
# -*- coding: utf-8 -*-
import click
from dugite.builders.skeleton import create_project_structure
from dugite.builders.supporting_files import initialize_files
from dugite.builders.controllers import generate_controller


@click.group()
def root():
    pass


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
