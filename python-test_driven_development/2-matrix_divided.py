#!/usr/bin/python3
"""
Docstring for python-test_driven_development.2-matrix_divided
"""


def matrix_divided(matrix, div):
    """
    Docstring for matrix_divided

    :param matrix: Description
    :param div: Description
    """
    terrm = "matrix must be a matrix (list of lists) of integers/floats"
    terrmrow = "Each row of the matrix must have the same size"
    new_matrix = []
    for row in matrix:
        if isinstance(row, list) is False:
            raise TypeError(terrm)
        if len(row) != len(matrix[0]):
            raise TypeError(terrmrow)
        temp = []
        for i in row:
            if isinstance(div, (int, float)) is False:
                raise TypeError("div must be a number")
            if div == 0:
                raise ZeroDivisionError("division by zero")
            temp.append(round(i / div, 2))
        new_matrix.append(temp)
        return new_matrix
