#!/usr/bin/python3
"""
Add an integer validator the class BaseGeometry
"""


class BaseGeometry:
    """
    Class for basic geometry
    """

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Method for checking if the argument is an positive integer

        :param self: recall of the class
        :param name: name of the parameter
        :param value: value of the integer
        """

        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
