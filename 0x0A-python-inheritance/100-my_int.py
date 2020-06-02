#!/usr/bin/python3
"""Myint Module
"""


class MyInt(int):
    """MyInt class"""

    def __eq__(self, other):
        """Reverse equality"""
        return super().__ne__(other)

    def __ne__(self, other):
        """Reverse difference"""
        return super().__eq__(other)
