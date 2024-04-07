#!/usr/bin/python3
"""Module 0-add_integer
Contains function add_integer: adds two integers
"""


def add_integer(a, b=98):
    """Adds two integers or floats

    Args:
        a (int, float): First number
        b (int, flaot): Second number

    Raises:
        TypeError: if either a or b is not an integer or flaot

    Returns:
        int: Sum of a and b
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
