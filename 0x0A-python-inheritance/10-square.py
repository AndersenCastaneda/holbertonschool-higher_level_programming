#!/usr/bin/python3
"""Square Module
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class"""

    def __init__(self, size):
        """Constructor
        Parameter:
            size
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """Returns object representation"""
        return super().__str__()

    def area(self):
        """returns object area"""
        return self.__size ** 2
