#!/usr/bin/python3
"""
python-classes.0-square
"""


class Square:
    """
    Declare a class named Square
    """

    def __init__(self, size=0):
        """
        Initialise the parameter for the class

        :param self: recall of itself
        :param size: size of the square
        """
        if isinstance(size, int) is False:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        """
        Getter for size

        :param self: recall of itself (Square)
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter for size

        :param self: recall of itself (Square)
        :param value: value to set to size
        """
        if isinstance(value, int) is False:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Area of the square

        :param self: recall of itself (Square)
        """
        return (self.__size * self.__size)
