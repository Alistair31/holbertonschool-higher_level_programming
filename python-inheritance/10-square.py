#!/usr/bin/python3
"""
Create a class Square that inherits from Rectangle.
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
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return f"[Rectangle] {self.__width}/{self.__height}"


class Square(Rectangle):
    """
    Class that defines a square inherited from Rectangle
    """

    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """
        Method for area of the square
        """
        return self.__size * self.__size

    def __str__(self):
        """
        String representation of the square
        """
        return f"[Rectangle] {self.__size}/{self.__size}"
