#!/usr/bin/python3
"""Square Module"""


class Square:
    """A Class used to represent an Square"""

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize Data.

        Argument:
            size: Size of a side of the square
        """
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """Retrieves the position"""
        return self.__position

    @position.setter
    def position(self, value):
        """
        Sets the position.

        Raises:
            TypeError: position must be a tuple of 2 positive integers
        """
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Returns square area"""
        return self.__size ** 2

    def my_print(self):
        """Prints the square using '#'
        prints the position using' '
        """
        pos = self.__position[0]
        if self.__size == 0:
            print()
        for i in range(self.__size):
            for j in range(pos):
                print(" ", end="")
            for k in range(self.__size):
                print("#", end="")
            print()
