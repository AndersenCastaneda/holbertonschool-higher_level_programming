#!/usr/bin/python3
"""read_file Module
"""


def read_file(filename=""):
    """Reads from filename and prints its contents to stdout.
    Parameters:
        filename: File's name
    """
    with open(filename) as file:
        print(file.read(), end="")
