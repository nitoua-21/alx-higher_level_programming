#!/usr/bin/python3
"""
Module 7-base_geometry

Contains class BaseGeometry
"""


class BaseGeometry():
    """Base class for geometry"""

    def area(self):
        """raises an Exception with the message area() is not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        validates value:
            if value is not an integer: raise a TypeError exception,
            with the message <name> must be an integer

            if value is less or equal to 0: raise a ValueError exception
            with the message <name> must be greater than 0

        Args:
            name (string): name
            value (int): value
        """

        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
