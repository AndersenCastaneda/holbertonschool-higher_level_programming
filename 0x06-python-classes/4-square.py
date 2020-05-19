#!/usr/bin/python3
"""Square Module"""


class Square:
    """A Class used to represent an Square"""

    def __init__(self, size=0):
        """
        Initialize Data.

        Argument:
            size: Size of a side of the square
        """
        self.__size = size

    def area(self):
        """Returns square area"""
        return self.__size ** 2

    @property
    def size(self):
        """Retrieves the value"""
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the value.

        Raises:
            TypeError: If size is not an integer
            ValueError: If size is less than 0
        """
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
