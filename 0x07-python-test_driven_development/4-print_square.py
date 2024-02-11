#!/bin/usr/python3

"""

This module defines a function that prints a square with the character #

"""


def print_square(size):
    """Prints a square with character #

    Raises:
        TypeError: if size is not an integer or is a negative float
        ValueError: if size is less than 0"""

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
