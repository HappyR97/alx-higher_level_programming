#!/usr/bin/python3

"""

This module defines a function that creates an object from a JSON file

"""

import json


def load_from_json_file(filename):
    """Creates object from JSON file"""
    with open(filename, encoding="utf-8") as file:
        return json.load(file)
