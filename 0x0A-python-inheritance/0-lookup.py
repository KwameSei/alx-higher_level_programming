#!/usr/bin/python3
"""Finds and returns a list of available attributes and methods of an object.
"""


def lookup(obj):

    """
    Returns a list of attributes and methods.
        Args:
            - obj: object to look into
    """
    return dir(obj)
