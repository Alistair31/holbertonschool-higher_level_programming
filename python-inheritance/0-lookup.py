#!/usr/bin/python3
"""
Function that display a list of available attribute and method of an object
"""


def lookup(obj):
    """
    Return every available attributes and methods of an object:

    :param obj: object to lookup
    """
    return dir(obj)
