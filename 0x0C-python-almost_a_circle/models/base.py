#!/usr/bin/python3
""" Base Module """
import json
import os.path as path


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
        """Returns the JSON string representation of list_dictionaries
        Parameters: list_dictionaries
        Raises:
            TypeError: list_dictionaries must be a list of dictionaries
        """
        if list_dictionaries in [[], None]:
            return "[]"
        if type(list_dictionaries) != list or not all(type(d) == dict for d in list_dictionaries):
            raise TypeError("list_dictionaries must be a list of dictionaries")
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation
        Parameters: json_string
        """
        if json_string is None or json_string == "":
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs
        to a file
        Parameters:
            cls: class instance
            list_object: list of object of type(cls)
        """
        if list_objs is None or list_objs == []:
            data = "[]"
        else:
            data = cls.to_json_string(
                [obj.to_dictionary() for obj in list_objs])
        filename = cls.__name__ + ".json"
        with open(filename, 'w') as file:
            file.write(data)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set
        Parameters:
            cls: class instance
            **dictionary: class info ((width, height) or size, x, y, id)
        """
        obj = cls(1, 1)
        obj.update(**dictionary)
        return obj

    @classmethod
    def load_from_file(cls):
        filename = cls.__name__ + ".json"
        objs = []
        dict_list = []
        if path.exists(filename):
            with open(filename, 'r') as file:
                dict_list = cls.from_json_string(file.read())
                for dictionary in dict_list:
                    objs.append(cls.create(**dictionary))
                file.close()
        return objs
