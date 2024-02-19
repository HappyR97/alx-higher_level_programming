#!/usr/bin/python3

"""

This module defines a class MyList that inherits for list

"""


class MyList(list):
    """class that inherits from list"""
    def print_sorted(self):
        """Prints the list in ascending order"""
        print(sorted(self))
