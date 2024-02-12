#!/usr/bin/python3

"""

This module defines a class Rectangle

"""


class Rectangle:
    """class that defines a rectangle"""
    def __init__(self, width=0, height=0):
        """"Initialize the data"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width with checks that it's an integer >= 0"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height with checks that it's an integer >= 0"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the rectangle area"""
        return self.__height * self.__width

    def perimeter(self):
        """Returns the retangle perimeter"""
        if self.__height == 0 or self.__width == 0:
            return 0
        return (self.__height + self.__width) * 2

    def __str__(self):
        """string representation of class"""
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            class_string = ""
            for i in range(self.__height):
                for j in range(self.__width):
                    class_string += "#"
                class_string += "\n"
        return class_string[:-1]

    def __repr__(self):
        """string representatin to be used with eval()"""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Prints deletion message"""
        print("Bye rectangle...")
