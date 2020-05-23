#!/usr/bin/python3
"""Calculation Module"""


def matrix_mul(m_a, m_b):
    """Multiply two matrix
    Parameters:
        m_a: must be a list of lists of integers or floats
        m_b: must be a list of lists of integers or floats
    Raises:
        TypeError: if m_a or m_b is not a list
        TypeError: if m_a or m_b is not a list of lists
        ValueError: if m_a or m_b is empty (it means: = [] or = [[]])
        TypeError: if one element of m_a or m_b matrices is not an
                   integer or a float
        TypeError: if m_a or m_b is not a rectangle
                   (all ‘rows’ should be of the same size)
        ValueError: if number of columns of m_a is different of the
                    number of rows of m_b
    Return:
        New Matrix whit the multiplication of m_a and m_b
    """
    if type(m_a) is not list:
        raise TypeError("m_a must be a list")

    if type(m_b) is not list:
        raise TypeError("m_b must be a list")

    for i in m_a:
        if type(i) is not list:
            raise TypeError("m_a must be a list of lists")

    for i in m_b:
        if type(i) is not list:
            raise TypeError("m_b must be a list of lists")

    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")

    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    for i in m_a:
        for j in i:
            if type(j) not in [int, float]:
                raise TypeError("m_a should contain only integers or floats")

    for i in m_b:
        for j in i:
            if type(j) not in [int, float]:
                raise TypeError("m_b should contain only integers or floats")

    length = len(m_a[0])
    for i in range(1, len(m_a)):
        if length != len(m_a[i]):
            raise TypeError("each row of m_a must be of the same size")

    length = len(m_b[0])
    for i in range(1, len(m_b)):
        if length != len(m_b[i]):
            raise TypeError("each row of m_b must be of the same size")

    columns = 0
    for i in m_a[0]:
        columns += 1

    rows = 0
    for i in m_b:
        rows += 1

    if columns != rows:
        raise ValueError("m_a and m_b can't be multiplied")

    result = [[0 for i in range(len(m_b[0]))] for j in range(len(m_a))]

    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            for k in range(len(m_b)):
                result[i][j] += m_a[i][k] * m_b[k][j]

    return result
