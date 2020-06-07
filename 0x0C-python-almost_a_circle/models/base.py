#!/usr/bin/python3
""" Base Module """
import json


class Base:
    """Base Class
    Private class attribute:
        __nb_objects: Number of instances (id)
    Public instance attribute:
        id: Object identifier
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Constructor
        Parameters: id
        Raises:
            TypeError: id must be an integer
        """
        if id is not None and type(id) != int:
            raise TypeError("id must be an integer")
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of
        list_dictionaries
        """
        if list_dictionaries in [[], None]:
            return "[]"
        if type(list_dictionaries) != list
        or not all(type(d) == dict for d in list_dictionaries):
            raise TypeError("list_dictionaries must be a list of dictionaries")
        return json.dumps(list_dictionaries)
