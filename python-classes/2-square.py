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
