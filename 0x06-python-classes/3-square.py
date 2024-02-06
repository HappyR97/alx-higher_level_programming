#!/usr/bin/python3

"""This module defines a class Square"""


class Square:
    """class Square that defines a square"""
    def __init__(self, size=0):
        """Initialize the data"""
        if isinstance(size, int):
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """Returns the current square area"""
        return self.__size ** 2
