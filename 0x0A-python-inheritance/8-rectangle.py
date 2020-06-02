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
