#!/usr/bin/python3
"""
Module 2-is_same_class
Contains function is_same_class
"""


def is_same_class(obj, a_class):
    """
     returns True if the object is exactly an instance
     of the specified class; otherwise False.

     Args:
        obj (object): object
        a_classs (class): a class
    """
    return type(obj) == a_class
