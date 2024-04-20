#!/usr/bin/python3
"""Module contains function is_kind_of_class(obj, a_class)"""


def is_kind_of_class(obj, a_class):
    """if the object is an instance of, or if the object is an instance of
        a class that inherited from, the specified class
    """
    return issubclass(type(obj), a_class)
