#!/usr/bin/python3
"""Square Module"""


class Square:
    """Represents a square.
    Private instance attribute: size:
        - property def size(self)
        - property setter def size(self, value)
    Private instance attribute: position:
        - property def position(self)
        - property setter def position(self, value)
    Instantiation with optional size and optional position.
    Public instance method: def area(self).
    Public instance method: def my_print(self).
    """

    def __init__(self, size=0, position=(0, 0)):
        """Initialize Data"""
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """Retrieves the value"""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the value"""
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
        """Sets the position"""
        if type(value) != tuple or len(value) != 2 or type(value[0]) != int or\
                type(value[1]) != int or value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Returns square area"""
        return self.__size ** 2

    def my_print(self):
        """Prints the square using '#' and position using ' '"""
        if self.__size == 0:
            print()
            return

        print("".join("\n" for i in range(self.__position[1])), end="")
        for i in range(self.__size):
            print("".join(" " for i in range(self.__position[0])), end="")
            print("".join("#" for i in range(self.__size)), end="")
            print()
