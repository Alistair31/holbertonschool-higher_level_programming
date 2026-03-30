#!/usr/bin/python3
"""
Module for dividing all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by div, rounded to 2 decimal places.

    Args:
        matrix: list of lists of integers or floats
        div: number (integer or float) to divide by

    Returns:
        A new matrix with all elements divided by div.

    Raises:
        TypeError: if matrix is not a list of lists of integers/floats
        TypeError: if rows of matrix don't all have the same size
        TypeError: if div is not a number
        ZeroDivisionError: if div is 0
    """
    terrm = "matrix must be a matrix (list of lists) of integers/floats"
    terrmrow = "Each row of the matrix must have the same size"

    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError(terrm)

    for row in matrix:
        for elem in row:
            if not isinstance(elem, (int, float)):
                raise TypeError(terrm)

    row_size = len(matrix[0]) if matrix else 0
    for row in matrix:
        if len(row) != row_size:
            raise TypeError(terrmrow)

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(elem / div, 2) for elem in row] for row in matrix]
