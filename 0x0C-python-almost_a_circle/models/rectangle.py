#!/usr/bin/python3
"""Rectangle Module"""
from models.base import Base


class Rectangle(Base):
    """Rectangle Class
    Private instances attribute: __width, __height, __x, __y
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Constructor
        Parameters: self, width, heigth, x, y, id
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    def __str__(self):
        """Object representation as string"""
        rep = "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height)
        return rep

    @property
    def width(self):
        """Returns width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets width
        Raises:
            TypeError: value must be an integer
            ValueError: value must be > 0
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Returns height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets height
        Raises:
            TypeError: value must be an integer
            ValueError: value must be > 0
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Returns x"""
        return self.__x

    @x.setter
    def x(self, value):
        """Sets x
        Raises:
            TypeValue: value must be an integer
            ValueError: value must be >= 0
        """
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Returns y"""
        return self.__y

    @y.setter
    def y(self, value):
        """Sets y
        Raises:
            TypeValue: value must be an integer
            ValueError: value must be >= 0
        """
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Returns area"""
        return self.__width * self.__height

    def display(self):
        """prints in stdout the Rectangle instance with the character #"""
        print("".join("\n" for i in range(self.__y)), end="")
        for i in range(self.__height):
            print("".join(" " for i in range(self.__x)), end="")
            print("".join("#" for i in range(self.__width)), end="")
            print()

    def update(self, *args, **kwargs):
        """Update Object info
        Parameters:
            *args: (id, width, height, x, y) respetivaly.
            **kwargs: {"id": , "width": , "height": , "x": , "y": }
        """
        if len(args) != 0:
            if len(args) >= 1:
                if args[0] is not None and type(args[0]) != int:
                    raise TypeError("id must be an integer")
                self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
            if len(args) >= 3:
                self.height = args[2]
            if len(args) >= 4:
                self.x = args[3]
            if len(args) >= 5:
                self.y = args[4]
        else:
            for key, value in kwargs.items():
                if key == "id":
                    if value is not None and type(value) != int:
                        raise TypeError("id must be an integer")
                    self.id = value
                elif key == "width":
                    self.width = value
                elif key == "height":
                    self.height = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """Returns the dictionary representation of the object"""
        d = {"id": self.id, "width": self.__width,
             "height": self.__height, "x": self.__x, "y": self.__y}
        return d
