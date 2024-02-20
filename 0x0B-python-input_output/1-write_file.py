#!/usr/bin/python3

"""

This module defines a function that writes a string to a text file

"""


def write_file(filename="", text=""):
    """Writes a string to a text file"""
    with open(filename, "w", encoding="UTF-8") as file:
        w = file.write(text)
        return w
