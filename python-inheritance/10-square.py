#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle
"""
Create a class Square that inherits from Rectangle.
"""


class Square(Rectangle):
    """
    Class that defines a square inherited from Rectangle
    """

    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
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
