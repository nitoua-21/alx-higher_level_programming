#!/usr/bin/python3
"""
Module 0-lookup
Contains function list
"""


def lookup(obj):
    """
    Returns the list of available attributes and methods of an object

    Args:
        obj (object): object

    Returns:
        List object
    """
    return dir(obj)
