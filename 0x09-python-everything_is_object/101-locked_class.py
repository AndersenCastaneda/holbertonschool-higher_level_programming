#!/usr/bin/python3
"""Locked class Module"""


class LockedClass:
    """Locked class"""
    __slots__ = ['first_name']

    def __init__(self, first_name=""):
        self.first_name = first_name
