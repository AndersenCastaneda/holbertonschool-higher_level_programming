#!/usr/bin/python3
def max_integer(my_list=[]):
    a = 0
    length = len(my_list)
    if length == a:
        return "None"

    for i in range(length):
        if my_list[i] > a:
            a = my_list[i]

    return a
