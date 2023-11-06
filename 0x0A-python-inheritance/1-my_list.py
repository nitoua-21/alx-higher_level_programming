#!/usr/bin/python3
"""
Module 1-my_list
Contains class MyList that inherits from list
"""


class MyList(list):
    """
    class MyList that inherits from list

    Args:
        list (object): list Data Structure
    """
    def print_sorted(self):
        """Prints sorted list"""
        print(sorted(self))
