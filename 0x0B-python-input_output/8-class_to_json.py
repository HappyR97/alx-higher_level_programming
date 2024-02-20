#!/usr/bin/python3

"""

This module defines a function that returns the dictionary description
for JSON serialization of an object

"""


def class_to_json(obj):
    """Returns dictionary description"""
    return obj.__dict__
