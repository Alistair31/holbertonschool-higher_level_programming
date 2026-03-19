#!/usr/bin/python3
"""
add two integer, convert non infinite and NaN float into
:param a: first integer to put in add function
:param b: second integer to put in add function
"""


def add_integer(a, b=98):
    """
    add two integer and return the result
    """
    if a == float('inf') or a == float('-inf') or a == float('NaN'):
        raise ValueError("a must be an integer")
    if isinstance(a, (int, float)) is False:
        raise TypeError("a must be an integer")
    if b == float('inf') or b == float('-inf') or b == float('NaN'):
        raise ValueError("b must be an integer")
    if isinstance(b, (int, float)) is False:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
