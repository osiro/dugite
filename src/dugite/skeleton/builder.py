#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os


def create_project_structure(project_name):
    skeleton = os.path.join(os.path.dirname(__file__), '..', 'assets',
                            'skeleton.txt')

    with open(skeleton, 'r') as file:
        for line in file:
            path = line.strip()
            if path:
                path = path.replace('my-app', project_name)
                if path.endswith('/'):
                    os.makedirs(path, exist_ok=True)
                else:
                    folder = os.path.dirname(path)
                    os.makedirs(folder, exist_ok=True)
                    with open(path, 'w'):
                        pass
