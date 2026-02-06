#!/usr/bin/python3
"""
check inheritance
"""


def inherits_from(obj, a_class):
    """
    Method for return if an object inheritance

    :param obj: object to check
    :param a_class: class to check
    """

    return issubclass(type(obj), a_class) and type(obj) is not a_class
