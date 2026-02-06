#!/usr/bin/python3
"""
Check if an object is in a class
"""


def is_same_class(obj, a_class):
    """
    Method for return true if the object is in the class

    :param obj: object to check
    :param a_class: class to check
    """

    return type(obj) is a_class
