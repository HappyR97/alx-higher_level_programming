#!/usr/bin/python3

"""

This module defines Student class

"""


class Student:
    """Defines Student class"""
    def __init__(self, first_name, last_name, age):
        """Inilializes values"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieves dictionary representation"""
        return self.__dict__
