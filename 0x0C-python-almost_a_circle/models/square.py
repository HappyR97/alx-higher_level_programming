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
