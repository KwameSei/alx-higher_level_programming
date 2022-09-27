#!/usr/bin/python3
"""Module 9-base_geometry.
Creates a Rectangle class."""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represents a rectangle
    Private instance attributes: width and height
    Inherits from BaseGeometry.
    """

    def __init__(self, width, height):
        """Initializes an instance
        Args:
        - width: the width of the rectangle
        - height: the height of the rectangle
        """
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """Returns a formatted string"""

        return str("[Rectangle] {:d}/{:d}".format(self.__width, self.__height))

    def area(self):
        """Gets the area of the Rectangle instance.
        Replaces the area() method from BaseGeometry.
        """

        return self.__height * self.__width
