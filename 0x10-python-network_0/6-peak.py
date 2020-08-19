#!/usr/bin/python3
"""Peak Module"""


def find_peak(loi):
    """Finds a peak in list_of_integers"""

    if loi is None or loi == []:
        return None

    left = 0
    right = len(loi) - 1

    # Return the maximum value of two elements
    if right == 0 or right == 1:
        return max(loi)

    # Cast to int
    mid = right // 2

    # If all elements has same value
    if loi[mid] >= loi[mid - 1] and loi[mid] >= loi[mid + 1]:
        return loi[mid]

    # Find a peak on the rigth half
    if loi[mid] < loi[mid + 1]:
        return find_peak(loi[mid:])

    # Find a peak on the left half
    if loi[mid] < loi[mid - 1]:
        return find_peak(loi[:mid])
