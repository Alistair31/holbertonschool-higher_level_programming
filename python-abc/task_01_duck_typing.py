#!/usr/bin/python3
from abc import ABC, abstractmethod
from math import pi
"""

"""


class Shape(ABC):
    """
    Shape
    """

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    """
    Circle shape
    """

    def __init__(self, radius):
        self.__radius = radius

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, value):
        self.__radius = value

    def area(self):
        return pi * (self.__radius ** 2)

    def perimeter(self):
        return 2 * pi * self.__radius


class Rectangle(Shape):
    """
    Rectangle shape
    """
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        return (self.__width * 2) + (self.__height * 2)


def shape_info(shape):
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
