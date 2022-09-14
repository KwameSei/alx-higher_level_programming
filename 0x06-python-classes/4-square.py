#!/usr/bin/python3

"""Define a class square"""


class Square:
    """Representation of square"""

    """Initialize a new square"""
    def __init__(self, size=0):
        self.__size = size

    """Defining area of a square"""
    def area(self):
        return self.__size**2

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        self.__size = value
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
