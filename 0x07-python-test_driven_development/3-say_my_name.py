#!/usr/bin/python3
"""Say my name Module"""


def say_my_name(first_name, last_name=""):
    """Prints My name is <first name> <last name>
        Parameters:
            first_name: must be a string
            last_name: must be a string
        Raises:
            TypeError: If first_name or last_name arr not a type string
    """
    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    if type(last_name) != str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
