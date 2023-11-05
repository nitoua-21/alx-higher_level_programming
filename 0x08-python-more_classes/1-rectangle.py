#!/usr/bin/python3
"""
Module 1-rectangle
Contains class Rectangle
With private attributes with and height
"""


class Rectangle():
    """
    A class represnting a rectangle

    Attributes:
        __width (int): width
        __height (int): height


    """
    def __init__(self, width=0, height=0):
        """
        Initializes a Rectangke with given width and height

        Args:
            width (int, optional): width of the rectangle. Defaults to 0.
            height (int, optional): height of the rectangle. Defaults to 0.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter method, returns width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter method, sets width if int value > 0"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter method, returns height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height, sets height if int value > 1"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
