#!/usr/bin/python3

"""

This module defines a funtion checks if object is an instance
of a class that inherited from specified class

"""


def is_kind_of_class(obj, a_class):
    """Returns True is same instance or inherited, otherwise False"""
    return isinstance(obj, a_class)
