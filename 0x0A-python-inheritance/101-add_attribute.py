#!/usr/bin/python3
"""Module add_attribute
"""


def add_attribute(obj, name, value):
    """"""
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
