#!/usr/bin/python3
"""Text identation Module"""


def text_indentation(text):
    """prints a text with 2 new lines after .?: characters
    Parameters:
        text: type string
        Raises:
            TypeError: text must be a string
    """
    if type(text) != str:
        raise TypeError("text must be a string")

    for c in ".?:":
        text = (c + "\n\n").join([line.strip(" ") for line in text.split(c)])
    print(text)

if __name__ == "__main__":
    text_indentation(". Hello,  :   wold ?      From python")
