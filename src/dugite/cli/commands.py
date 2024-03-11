#!/usr/bin/env python
# -*- coding: utf-8 -*-
import click


@click.group()
def root():
    pass


@click.command(name="new", help="Create a new project.")
@click.argument('name')
def initializer(name):
    click.echo(f'Initializing project {name}')


@click.group(name="g", help="Generate project components.")
def generator(_):
    click.echo('Generate something')


@click.command(name="controller", help="Generate a controller.")
def controller_generator(_):
    click.echo('Generate controller')


@click.command(name="model", help="Generate a model.")
def model_generator(_):
    click.echo('Generate model')


root.add_command(initializer)
root.add_command(generator)
generator.add_command(controller_generator)
generator.add_command(model_generator)
