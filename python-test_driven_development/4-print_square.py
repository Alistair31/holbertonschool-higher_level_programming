#!/usr/bin/python3
"""
Docstring for python-test_driven_development.4-print_square
"""


def print_square(size):
    """
    Docstring for print_square

    :param size: Description
    """
    if isinstance(size, int) is False:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(0, size):
        for j in range(0, size):
            print("#", end="")
        print()
