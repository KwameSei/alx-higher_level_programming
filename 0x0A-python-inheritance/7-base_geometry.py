#!/usr/bin/python3
"""Module 5-base_geometry.
Creates a class."""


class BaseGeometry:
    """Class with public instance method"""

    def area(self):
        """Raises an Exception with the following message
        """
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """Validate value"""

        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
