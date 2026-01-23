#!/usr/bin/python3
'''
Docstring for 0-add_integer
'''


def add_integer(a, b=98):
    '''
    Docstring for add_integer
    :param a: first integer to put in add function
    :param b: second integer to put in add function
    '''
    if a == float('inf') or a == float('-inf'):
        raise ValueError("a must be an integer")
    if isinstance(a, (int, float)) is False:
        raise TypeError("a must be an integer")
    if b == float('inf') or b == float('-inf'):
        raise ValueError("b must be an integer")
    if isinstance(b, (int, float)) is False:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
