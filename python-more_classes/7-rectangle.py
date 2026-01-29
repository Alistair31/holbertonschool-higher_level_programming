#!/usr/bin/python3
"""
python-more_classes.0-rectangle
"""


class Rectangle:
    """
    define a class named Rectangle
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initialise the parameter for the class

        :param self: recall of itself
        :param width: width of the rectangle
        :param height: heigth of the rectangle
        """
        if isinstance(width, int) is False:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if isinstance(height, int) is False:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """
        Getter for width

        :param self: recall of itself (rectangle)
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter for width

        :param self: recall of itself (rectangle)
        :param value: value to set to width
        """
        if isinstance(value, int) is False:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Getter for height

        :param self: recall of itself (rectangle)
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter for height

        :param self: recall of itself (rectangle)
        :param value: value to set to heigth
        """
        if isinstance(value, int) is False:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Area of the rectangle

        :param self: recall of itself (rectangle)
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Perimeter of the rectangle

        :param self: recall of itself (rectangle)
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return self.__width * 2 + self.__height * 2

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        list = []
        for _ in range(self.__height):
            list.append(str(self.print_symbol) * self.__width)
        return "\n".join(list)

    def __repr__(self):
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
