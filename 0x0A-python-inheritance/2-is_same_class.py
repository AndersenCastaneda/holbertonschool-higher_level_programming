#!/usr/bin/python3
"""Module is_same_class
"""


def is_same_class(obj, a_class):
    """Check if an obejct is the same class.
    Parameters:
        obj: Instance to compare
        a_class: class to compare
    Return: True if obj is the same type of a_class, otherwise False
    """
    return type(obj) == a_class
