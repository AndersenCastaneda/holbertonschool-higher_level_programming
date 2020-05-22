#!/usr/bin/python3
"""Print Square Module"""


def print_square(size):
    """Prints a square with the character #.
    Parameters:
        size: must be type integer
    Raises:
        TypeError: size must be an integer
        ValueError: size must be >= 0
    """
    if type(size) != int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("".join("#" for j in range(size)))
