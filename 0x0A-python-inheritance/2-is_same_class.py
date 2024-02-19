#!/usr/bin/python3

"""

This module defines a funtion checks if object
is same instance of another class

"""


def is_same_class(obj, a_class):
    """Returns True is same instance, otherwise False"""
    return isinstance(obj, a_class)
