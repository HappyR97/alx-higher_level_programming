#!/usr/bin/python3

"""

This module defines a Base class

"""

import json


class Base:
    """Defines Base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes Base"""
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns JSON string representation"""
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string to a file"""
        filename = cls.__name__ + ".json"
        list_dicts = (
                [obj.to_dictionary() for obj in list_objs]
                if list_objs else []
        )
        with open(filename, "w") as file:
            json.dump(list_dicts, file)

    @staticmethod
    def from_json_string(json_string):
        """Returns list of JSON string"""
        if json_string is None or json_string == "":
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes set"""
        if cls.__name__ == "Rectangle":
            dummy_instance = cls(1, 1)
        elif cls.__name == "Square":
            dummy_instance = cls(1)
        dummy_instance.update(**dictionary)
        return dummy_instance
