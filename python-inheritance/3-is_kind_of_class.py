#!/usr/bin/python3
"""
Check if the object is an instance of class or an inherited class
"""


def is_kind_of_class(obj, a_class):
    """
    Method for check if an object is in a class or inherited class

    :param obj: object to check
    :param a_class: class to check
    """

    if isinstance(obj, a_class) is True:
        return True
