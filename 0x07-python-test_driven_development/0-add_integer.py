#!/usr/bin/python3

"""

This module defines a function that adds 2 numbers

"""


def add_integer(a, b=98):

    """ Returns additions of two numbers (int)
        Raises:
            TypeError: If a or b are not ints or floats"""

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
