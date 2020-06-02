#!/usr/bin/python3
"""MyList module
"""


class MyList(list):
    """MyList class.
    Public instance method:
        def print_sorted(self):
    """

    def print_sorted(self):
        """Sort MyList object and prints"""
        sorted_list = self[:]
        sorted_list.sort()
        print("{}".format(sorted_list))
