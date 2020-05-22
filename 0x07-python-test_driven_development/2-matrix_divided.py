#!/usr/bin/python3
"""Calculation Module
Funtions:
    matrix_divided: divides all elements of a matrix
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of the matrix.
    Parameters:
        matrix: list of lists of integers/floats
        div: must be integer or float
    Raises:
        TypeError: If matrix is not a matrix (list of lists) of integers/floats
        TypeError: Each row of the matrix must have the same size
        TypeError: If div is not an integer or float
        TypeError: ZeroDivisionError
    Returns:
        Integer: The addition of a and b
    """
    if type(matrix) != list or len(matrix) == 0 or not matrix[0]:
        raise TypeError("matrix must be a matrix (list of lists) of integers" +
                        "/floats")

    count = len(matrix[0])
    for i in range(1, len(matrix)):
        if type(matrix[i]) != list:
            raise TypeError("matrix must be a matrix (list of lists) of " +
                            "integers/floats")

        for num in matrix[i]:
            if type(num) not in [int, float]:
                raise TypeError("matrix must be a matrix (list of lists)" +
                                "of integers/floats")

        if count != len(matrix[i]):
            raise TypeError("Each row of the matrix must have the same size")
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [[round(x / div, 2) for x in row] for row in matrix]
    return new_matrix
