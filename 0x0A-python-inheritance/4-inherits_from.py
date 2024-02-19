#!/usr/bin/python3

"""

This module defines inherits_from function

"""


def inherits_from(obj, a_class):
    """Checks if an object is a true subclass of a class"""
    return isinstance(obj, a_class) and type(obj) is not a_class
