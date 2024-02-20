#!/usr/bin/python3

"""

This module defines a function that writes
an Objet to a text file, using JSON representation

"""

import json


def save_to_json_file(my_obj, filename):
    """Writes to file using JSON representation"""
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(my_obj, file)
