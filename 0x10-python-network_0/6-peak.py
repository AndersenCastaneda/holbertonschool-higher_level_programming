#!/usr/bin/python3
"""Peak Module"""


def find_peak(loi):
    """Finds a peak in list_of_integers"""

    if loi is None or loi == []:
        return None

    left = 0
    right = len(loi) - 1

    # Limit overflow
    mid = left + ((right - left) // 2)

    # If is only one element
    if right == 1:
        return loi[0]

    # If there is only two elements return the bigger one
    if right == 2:
        return loi[0] if loi[0] > loi[1] else loi[1]

    # If all elements has same value
    if loi[mid] >= loi[mid - 1] and loi[mid] >= loi[mid + 1]:
        return loi[mid]

    # Find a peak on the rigth half
    if mid > 0 and loi[mid] < loi[mid + 1]:
        return find_peak(loi[mid:])

    # Find a peak on the left half
    if mid > 0 and loi[mid] < loi[mid - 1]:
        return find_peak(loi[:mid])
