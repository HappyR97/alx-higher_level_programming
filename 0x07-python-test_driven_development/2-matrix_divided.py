#!/usr/bin/python3

"""

This module defines a functions that divides all elements of a matrix

"""


def matrix_divided(matrix, div):

    """ Returns a new matrix resulting from division of matrix
        Raises:
            TypeError: if 'matrix' is not a matrix of a matrix
                    of integers/floats
                       if rows do not have same size
                       if 'div' is not a number
            ZeroDivisionError: if we divide by zero"""

    error_text = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(matrix, list) or not matrix:
        raise TypeError(error_text)
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError(error_text)
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError(error_text)

    row_size = len(matrix[0])
    for row in matrix:
        if len(row) != row_size:
            raise TypeError("Each row of the matrix must have the same size")

    new_matrix = []
    for row in matrix:
        new_row = []
        for element in row:
            new_row.append(round(element / div, 2))
        new_matrix.append(new_row)

    return new_matrix
