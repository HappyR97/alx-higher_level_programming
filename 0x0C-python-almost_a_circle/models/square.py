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

    def __str__(self):
        """Returns string representation of Square"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
