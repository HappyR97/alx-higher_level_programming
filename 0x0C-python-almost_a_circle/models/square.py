#!/usr/bin/python3

"""

This module defines a Square class that inherits from Rectangle

"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Defines Square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes Square"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter for size"""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for size"""
        self.width = value
        self.height = value

    def __str__(self):
        """Returns string representation of Square"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    def update(self, *args, **kwargs):
        """Updates the attributes of the Square instance."""
        if args:
            attributes = ['id', 'size', 'x', 'y']
            for i, value in enumerate(args):
                setattr(self, attributes[i], value)
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dictionnary representation of a Square"""
        my_dict = {
                "id": self.id,
                "size": self.width,
                "x": self.x,
                "y": self.y
                }
        return my_dict
