#!/usr/bin/python3

"""

This module defines class BaseGeometry

"""


class BaseGeometry:
    """BaseGeometry class"""
    def area(self):
        """Raises an Exception with a message"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates value
        Raises: TypeError if value is not an integer
                ValueError if value is less or equal to 0"""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
