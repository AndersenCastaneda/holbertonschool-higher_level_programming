#!/usr/bin/python3
"""BaseGeometry Module
"""


class BaseGeometry:
    """BaseGeometry class
    Public instance method:
        def area(self):
        def integer_validator(self, name, value):
    """

    def area(self):
        """Raises Exception area() is not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates value"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
