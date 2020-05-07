#!/usr/bin/python3
def uniq_add(my_list=[]):
    numbers = set(my_list)
    sum = 0
    for number in numbers:
        sum += number
    return sum
