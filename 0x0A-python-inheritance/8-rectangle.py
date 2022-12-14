#!/usr/bin/python3
"""Module 8-base_geometry.
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
