#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import subprocess
import click


def generate_lambda_function(controller_folder):
    lambda_function_template = os.path.join(
        os.path.dirname(__file__), '..', 'assets', 'lambda_function.py')

    with open(lambda_function_template, 'r') as content:
        with open(os.path.join(controller_folder, 'lambda.py'), 'w') as file:
            file.write(content.read())


def generate_requirements_file(controller_folder):
    requirements_file_template = os.path.join(
        os.path.dirname(__file__), '..', 'assets', 'requirements.txt')

    with open(requirements_file_template, 'r') as content:
        with open(os.path.join(
            controller_folder, 'requirements.txt'), 'w') as file:
            file.write(content.read())


def initialize_virtual_env(controller_folder):
    os.chdir(controller_folder)
    try:
        command = """
python -m venv .env && \\
source .env/bin/activate && \\
pip install -r requirements.txt
"""

        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        click.echo(f"Error: {e}")


def generate_controller(name):
    controller_folder = os.path.join('app', 'controllers', name)
    os.makedirs(controller_folder)

    generate_lambda_function(controller_folder)
    generate_requirements_file(controller_folder)
    initialize_virtual_env(controller_folder)
