#!/usr/bin/python3
"""Scuare Module"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square Class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Constructor
        Parameters: self, size, x, y, id
        """
        self.size = size
        super().__init__(self.size, self.size, x, y, id)

    def __str__(self):
        """Object representation as string"""
        rep = "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.size)
        return rep

    @property
    def size(self):
        """Return size"""
        return self.__width

    @size.setter
    def size(self, value):
        """Sets size
        Raises:
            TypeError: value must be an integer
            ValueError: value must be > 0
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value
        self.__height = value

    def update(self, *args, **kwargs):
        """Update Object info
        Parameters:
            *args: (id, size, x, y) respetivaly.
            **kwargs: {"id": , "size": , "x": , "y": }
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
        else:
            for key, value in kwargs.items():
                if key == "id":
                    if value is not None and type(value) != int:
                        raise TypeError("id must be an integer")
                    self.id = value
                elif key == "size":
                    self.size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """Returns the dictionary representation of the object"""
        d = {"id": self.id, "size": self.size, "x": self.x, "y": self.y}
        return d
