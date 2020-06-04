#!/usr/bin/python3
""" append_write Module """


def append_write(filename="", text=""):
    """Appends a string at the end of a text file (UTF8)
    Parameters:
        file_name: File's name
        text: Text to append
    Return: Number of characters added
    """
    with open(filename, 'a') as file:
        return file.write(text)
