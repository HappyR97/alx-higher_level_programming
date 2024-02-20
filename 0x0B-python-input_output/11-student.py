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

    def to_json(self, attrs=None):
        """Retrieves dictionary representation"""
        if attrs is None:
            return self.__dict__
        return {key: value for key, value in self.__dict__.items()
                if key in attrs}

    def reload_from_json(self, json):
        """Replaces all attributes"""
        for key, value in json.items():
            setattr(self, key, value)
