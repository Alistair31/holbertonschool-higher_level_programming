#!/usr/bin/python3
"""
5-base_geometry: 1st step of creating a class BaseGeometry
"""


class BaseGeometry:
    """
    Class for basic geometry
    """

    def __init__(self):
        pass

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Docstring for integer_validator

        :param self: Description
        :param name: Description
        :param value: Description
        """

        if isinstance(value, int) is False:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
