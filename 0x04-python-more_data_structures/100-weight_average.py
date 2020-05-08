#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    avg = 0
    div = 0
    for i, j in my_list:
        avg += i * j
        div += j
    return avg / div
