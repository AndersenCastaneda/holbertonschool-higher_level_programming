#!/usr/bin/python3
"""Module is_kind_of_class
"""


def is_kind_of_class(obj, a_class):
    """Check if an obejct is an instance of a class, or if is
    an instance of a class that inheritence from.
    Parameters:
        obj: Instance to compare
        a_class: class to compare
    Return: True if obj is the same type of a_class, otherwise False
    """
    return isinstance(obj, a_class)
