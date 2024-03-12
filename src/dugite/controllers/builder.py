#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os


def generate_lambda_function(controller_folder):
    lambda_function_template = os.path.join(
        os.path.dirname(__file__), '..', 'assets', 'lambda_function.py')

    with open(lambda_function_template, 'r') as content:
        with open(os.path.join(controller_folder, "lambda.py"), "w") as file:
            file.write(content.read())


def generate_controller(name):
    controller_folder = os.path.join('app', 'controllers', name)
    os.makedirs(controller_folder)

    generate_lambda_function(controller_folder)
