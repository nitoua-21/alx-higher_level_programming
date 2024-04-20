#!/usr/bin/python3
"""Contains a class MyList that that inherits from list"""


class MyList(list):
    """inherits from list."""

    def print_sorted(self):
        """prints the list, but sorted (ascending sort)"""
        print(sorted(self))
