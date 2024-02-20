#!/usr/bin/python3

"""

This module defines a function that appends a string to to text file

"""


def append_write(filename="", text=""):
    """Appends text to file"""
    with open(filename, "a", encoding="UTF-8") as file:
        a = file.write(text)
        return a
