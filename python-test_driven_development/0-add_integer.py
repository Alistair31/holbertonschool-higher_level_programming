#!/usr/bin/python3
def add_integer(a, b=98):
    """
    Docstring for add_integer
    :param a: Description
    :param b: Description
    """
    if isinstance(a, (int, float)) is False:
        if isinstance(a, float) is True:
            if a == float('inf') or a == float('-inf'):
                raise ValueError("a must be an integer")
        raise TypeError("a must be an integer")
    if isinstance(b, (int, float)) is False:
        if isinstance(b, float) is True:
            if b == float('inf') or b == float('-inf'):
                raise ValueError("b must be an integer")
        raise TypeError("b must be an integer")
    return int(a) + int(b)
