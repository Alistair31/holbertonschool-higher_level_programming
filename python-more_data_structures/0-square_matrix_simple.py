#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    squared = matrix
    for i, j in range(len(matrix)):
        squared[i, j] = matrix[(i ** 2), (j ** 2)]
        return squared
