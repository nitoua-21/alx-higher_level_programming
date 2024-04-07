#!/usr/bin/python3
"""Module 2-matrix_divided
Contains function matrix_divided that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix by a number.

    Args:
        matrix (list of lists): matrix to be divided
        div (int, float): divider

    Raises:
        TypeError: if matrix is not a list of lists of integers/floats,
            if each row of the matrix does not have the same size,
            or if div is not an integer/float.

        ZeroDivisionError: if div = 0

    Returns:
        A new matrix with all elements divided by div,
                        rounded to 2 decimal places.
    """

    # Check if matrix is a list of lists of integers or floats
    if not isinstance(matrix, list) or \
        not all(isinstance(row, list) for row in matrix) or \
            not all(isinstance(num, (int, float))
                    for row in matrix for num in row):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")

    # Check if all rows are lists and have the same size
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    # Check if div is a number (integer or float)
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Check if div is not equal to 0
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(num / div, 2) for num in row] for row in matrix]
