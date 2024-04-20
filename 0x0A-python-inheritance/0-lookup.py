#!/usr/bin/python3
"""Module to return the list of available attributes
    and methods of an object
"""


def lookup(obj):
    """returns the list of available attributes and methods of object"""
    return dir(obj)
