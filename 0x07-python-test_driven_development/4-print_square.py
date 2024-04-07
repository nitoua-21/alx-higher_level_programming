#!/usr/bin/python3
"""Module 4-print_square
Contains function print_square(size)
"""


def print_square(size):
    """Prints a square with the character #, given the siz

    Args:
        size (int):  size length of the square

    Raises:
        TypeError: if size is not an integer or a float less than 0.

        ValueError: if size is less than 0
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    if size == 0:
        print("", end="")
    else:
        for _ in range(size):
            print("#" * size)
