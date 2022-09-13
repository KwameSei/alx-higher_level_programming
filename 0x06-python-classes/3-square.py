#!/usr/bin/python3

"""Define a class square"""


class Square:
    """Representation of square"""

    """Initialize a new square"""
    def __init__(self, size=0):
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    """Defining area of a square"""
    def area(self):
        return self.__size**2
