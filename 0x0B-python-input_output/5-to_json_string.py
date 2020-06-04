#!/usr/bin/python3
""" to_json_string Module """
import json


def to_json_string(my_obj):
    """Returns the JSON representation of an object
    Parameters:
        my_obj: Object
    Return: Representation of an object (string)
    """
    return json.dumps(my_obj)
