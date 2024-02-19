#!/usr/bin/python3

"""

This modules defines a function that checks if
the object is an instance of a class that inherited
from a specified class

"""


def inherits_from(obj, a_class):
    """Checks if an object is a true subclass of a class"""
    return isinstance(obj, a_class) and type(obj) is not a_class
