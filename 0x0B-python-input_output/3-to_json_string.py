#!/usr/bin/python3

"""

This module defines a function that returns JSON representation of an object

"""

import json


def to_json_string(my_obj):
    """Returns JSON representation of an object"""
    json_string = json.dumps(my_obj)
    return json_string
