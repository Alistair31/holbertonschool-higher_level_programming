#!/usr/bin/python3
"""
5-base_geometry: 1st step of creating a class BaseGeometry
"""


class BaseGeometry:
    """
    Class for basic geometry
    """

    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Method for checking if the argument is an positive integer

        :param self: recall of the class
        :param name: name of the parameter
        :param value: value of the integer
        """

        if isinstance(value, int) is False:
            raise TypeError(f"{name} must be an integer")
        if isinstance(self.__width, int) is False:
            raise TypeError("width must be an integer")
        if isinstance(self.__height, int) is False:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
        if self.__width <= 0:
            raise ValueError("width must be greater than 0")
        if self.__height <= 0:
            raise ValueError("height must be greater than 0")


class Rectangle(BaseGeometry):
    """
    class that define a rectangle
    """

    def __init__(self, width, height):
        """
        initialisation of the class

        :param self: recall of itself
        :param width: width of the rectangle
        :param height: height of the rectangle
        """

        self.__width = width
        self.__height = height
        if type(self.__width) is not int:
            raise TypeError("width must be an integer")
        if type(self.__height) is not int:
            raise TypeError("height must be an integer")
        if self.__width <= 0:
            raise ValueError("width must be greater than 0")
        if self.__height <= 0:
            raise ValueError("height must be greater than 0")

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return f"[Rectangle] {self.__width}/{self.__height}"
