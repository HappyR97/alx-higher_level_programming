#!/usr/bin/python3

"""

This module defines a function that reads from a text file
and prints it to stdout

"""


def read_file(filename=""):
    with open(filename, encoding='UTF8') as file:
        text = file.read()
        print(text)
