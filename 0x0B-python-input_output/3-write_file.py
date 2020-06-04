#!/usr/bin/python3
""" write_file Module """


def write_file(filename="", text=""):
    """Writes text in filename.
    Parameters:
        filename: File's name
        text: Text to write
    Return: number of characters written
    """
    with open(filename, 'w') as file:
        return file.write(text)
