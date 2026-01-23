#!/usr/bin/python3
"""
Docstring for python-test_driven_development.3-say_my_name
"""


def say_my_name(first_name, last_name=""):
    """
    Docstring for say_my_name
    :param first_name: Description
    :param last_name: Description
    """
    if isinstance(first_name, str) is False:
        raise TypeError("first_name must be a string")
    if isinstance(last_name, str) is False:
        raise TypeError("last_name must be a string")
    if last_name == "":
        print("My name is {}".format(first_name))
    else:
        print("My name is {} {}".format(first_name, last_name))
