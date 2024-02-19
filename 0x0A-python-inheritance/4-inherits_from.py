#!/usr/bin/python3

"""

This modules defines a function that checks if
the object is an instance of a class that inherited
from a specified class

"""


def inherits_from(obj, a_class):
    """
    Returns True of obj is instance of a class that inherited
    from a_class
    """

    return issubclass(type(obj), a_class)
