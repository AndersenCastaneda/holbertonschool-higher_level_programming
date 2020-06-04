#!/usr/bin/python3
""" from_json_string Module """
import json


def from_json_string(my_str):
    """Returns an object (Python data structure) represented by a JSON"""
    return json.loads(my_str)
