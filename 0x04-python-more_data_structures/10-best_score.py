#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    m = None
    for i in a_dictionary:
        if not m or a_dictionary[i] > a_dictionary[m]:
            m = i
    return m
