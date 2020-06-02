#!/usr/bin/python3
"""Rectangle Module
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class
    Inherits:
        BaseGeometry
    Private instance attribute:
        width
        height
    """

    def __init__(self, width, height):
        """Constructor.
        Parameters:
            width
            height
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """Returns object representation"""
        return str("[Rectagle] {}/{}".format(self.__width, self.__height))

    def area(self):
        """returns object area"""
        return self.__width * self.__height
