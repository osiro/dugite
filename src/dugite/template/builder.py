#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from jinja2 import Environment, FileSystemLoader


def generate_readme(project_name, python_version, terraform_version):
    env = Environment(loader=FileSystemLoader(
        os.path.join(os.path.dirname(__file__), '..', 'assets')))
    template = env.get_template('README.md')

    content = template.render(
        project_name=project_name,
        python_version=python_version,
        terraform_version=terraform_version)

    with open(os.path.join(project_name, "README.md"), "w") as file:
        file.write(content)


def generate_gitignore(project_name):
    content = """
.env
terraform/.terraform
__pycache__
""".strip()

    with open(os.path.join(project_name, ".gitignore"), "w") as file:
        file.write(content)


def generate_python_version(project_name, version):
    with open(os.path.join(project_name, ".python-version"),
              "w") as file:
        file.write(version)


def generate_terraform_version(project_name, version):
    with open(os.path.join(project_name, "terraform", ".terraform-version"),
              "w") as file:
        file.write(version)


def initialize_files(project_name, python_version, terraform_version):
    generate_gitignore(project_name)
    generate_python_version(project_name, python_version)
    generate_terraform_version(project_name, terraform_version)
    generate_readme(project_name, python_version, terraform_version)
