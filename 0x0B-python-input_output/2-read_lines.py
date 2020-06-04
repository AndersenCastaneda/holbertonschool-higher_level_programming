#!/usr/bin/python3
""" read_lines Module """


def read_lines(filename="", nb_lines=0):
    """Reads and prints nb_lines lines from filename.
    Parameters:
        filename: File's name
        nb_lines: File's number lines
    """
    with open(filename, 'r') as file:
        if nb_lines <= 0:
            print(file.read(), end="")
        else:
            lines = 0
            for i in file:
                print(i, end='')
                lines += 1
                if lines == nb_lines:
                    break
