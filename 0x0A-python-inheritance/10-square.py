#!/usr/bin/python3

"""

This module defines a Square class

"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Square subclass of Rectangle """
    def __init__(self, size):
        """Initializes values"""
        self.integer_validator("size", size)

        self.__size = size
        super().__init__(size, size)

    def area(self):
        """ Returns area """
        return self.__size ** 2
