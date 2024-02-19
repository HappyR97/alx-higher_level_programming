#!/usr/bin/python3

"""

This module defines a function that returns
a list of available attributes and methods of an object

"""


def lookup(obj):
    """ Returns available attributes and methods """
    return dir(obj)
