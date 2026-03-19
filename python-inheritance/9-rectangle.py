#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""
Add an area method to class BaseGeometry
"""


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
