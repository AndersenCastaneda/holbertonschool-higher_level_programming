#!/usr/bin/python3
"""Rectangle class
"""


class Rectangle:
    """Rectangle.
    Private instance attribute: width:
        Property def width(self): Returns width
        Property setter def width(self, value): Sets width = value
    Private instance attribute: height:
        Property def height(self): Return heigth
        Property setter def height(self, value): Sets height = value
    Public class attribute:
        number_of_instances = 0
        print_symbol = "#"
    Public instance method:
        def area(self): Returns rectangle area
        def perimeter(self): Returns rectangle perimeter
    Public static method:
        def bigger_or_equal(rect_1, rect_2):
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize Object"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __str__(self):
        """Returns rectangle representation"""
        if self.__width == 0 or self.__height == 0:
            return ""
        s = ""
        for i in range(self.__height):
            for j in range(self.__width):
                s += str(self.print_symbol)
            if i != self.__height - 1:
                s += "\n"
        return s

    def __repr__(self):
        """Returns rectangle representation"""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Prints Bye Message, decrease number of instances count"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Compare 2 rectangles and returns the biggest one"""
        if type(rect_1) != Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) != Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        return rect_1 if rect_1.area() >= rect_2.area() else rect_2

    @property
    def width(self):
        """Returns width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets width"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(selg):
        """Returns heigth"""
        return self.__heigth

    @height.setter
    def height(self, value):
        """Sets heigth"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns area"""
        return self.__width * self.__height

    def perimeter(self):
        """Returns perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)
