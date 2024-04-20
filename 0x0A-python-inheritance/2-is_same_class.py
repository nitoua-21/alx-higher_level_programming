#!/usr/bin/python3
"""Contains function is_same_class """


def is_same_class(obj, a_class):
    """Checks if the object is exactly
        an instance of the specified class
    """

    return type(obj) is a_class
