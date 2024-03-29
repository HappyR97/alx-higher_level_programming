#!/usr/bin/python3

"""This module defines a class Square"""


class Square:
    """class Square that defines a square"""
    def __init__(self, size=0):
        """Initialize the data"""
        self.__size = size

    @property
    def size(self):
        """Getter for size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for radius, with checks that it's a non negative int"""
        if isinstance(value, int):
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """Returns the current square area"""
        return self.__size ** 2
