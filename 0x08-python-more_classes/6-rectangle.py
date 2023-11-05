#!/usr/bin/python3
"""
Module 6-rectangle
Contains class Rectangle
With private attributes with and height
"""


class Rectangle():
    """
    A class represnting a rectangle

    Attributes:
        __width (int): width
        __height (int): height
        number_of_instances (int): number of instances


    """
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """
        Initializes a Rectangke with given width and height

        Args:
            width (int, optional): width of the rectangle. Defaults to 0.
            height (int, optional): height of the rectangle. Defaults to 0.
        """
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    def __del__(self):
        """ Deletes instance of class """
        print("Bye rectangle...")
        type(self).number_of_instance -= 1

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

    def area(self):
        """Calculates and returns the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Calculates and returns the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """ Prints rectangle with #'s """
        if self.__width == 0 or self.__height == 0:
            return ""
        pic = "\n".join(["#" * self.__width for rows in range(self.__height)])
        return pic

    def __repr__(self):
        """ String representation to recreate new instance """
        return "Rectangle({:d}, {:d})".format(self.width, self.height)
