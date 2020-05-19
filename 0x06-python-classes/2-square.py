#!/usr/bin/python3
"""Square Module"""


class Square:
    """A Class used to represent an Square"""

    def __init__(self, size=0):
        """
        Initialize Data.

        Argument:
            size: Size of a side of the square

        Raises:
            TypeError: If size is not an integer
            ValueError: If size is less than 0
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
