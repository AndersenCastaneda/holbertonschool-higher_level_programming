#!/usr/bin/python3
"""Module inherits_froms
"""


def inherits_from(obj, a_class):
    """Check if  the object is an instance of a class that inherited
    (directly or indirectly) from the specified class
    Parameters:
        obj: Instance to compare
        a_class: class to compare
    Return: True if obj is the same type of a_class, otherwise False
    """
    return isinstance(obj, a_class) and type(obj) != a_class
