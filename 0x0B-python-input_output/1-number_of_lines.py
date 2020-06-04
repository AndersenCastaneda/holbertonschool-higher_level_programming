#!/usr/bin/python3
"""number_of_lines Module
"""


def number_of_lines(filename=""):
    """Counts lines in filename.
    Parameters:
        filename: File's name
    Return:
        number of lines
    """
    lines = 0
    with open(filename) as file:
        txt = file.readlines()
    return len(txt)
