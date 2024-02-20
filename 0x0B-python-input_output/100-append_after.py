#!/usr/bin/python3

"""

This module defines a function that inserts a line of text to a file,
after each line containing a specific string

"""


def append_after(filename="", search_string="", new_string=""):
    """Inserts a line to file if specific string is found"""
    with open(filename, "r+", encoding="utf-8") as file:
        lines = file.readlines()
        for i in range(len(lines)):
            if search_string in lines[i]:
                lines.insert(i + 1, new_string)
            i += 1
        file.seek(0)
        file.writelines(lines)
