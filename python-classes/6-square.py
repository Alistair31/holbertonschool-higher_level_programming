#!/usr/bin/python3
"""
python-classes.0-square
"""


class Square:

    def __init__(self, size=0,  position=(0, 0)):
        if isinstance(size, int) is False:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        self.__position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if isinstance(value, int) is False:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return self.__size

    @position.setter
    def position(self, value):
        if isinstance(value, tuple(0, 0)) is False and value[0, 1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        return (self.__size * self.__size)

    def my_print(self):
        if self.__size == 0:
            print()
        #if int(self.__position[1]) > 0:
        for _ in range(0, self.__size):
            for _ in range(0, self.__position[0]):
                print(" " * self.__position[0], end="")
                print("#" * self.__size)
