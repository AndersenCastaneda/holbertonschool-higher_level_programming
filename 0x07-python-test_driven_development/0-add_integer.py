#!/usr/bin/python3
"""Calculation Module
Funtions:
    add_integer: Adds two integers
"""


def add_integer(a, b=98):
    """
    Adds two integers.
    Parameters:
        a: must be integer or float
        b: must be integer or float
    Raises:
        TypeError: If a or b are not integers or floats
    Returns:
        Integer: The addition of a and b
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")

    return int(a) + int(b)
