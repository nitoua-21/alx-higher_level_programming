#!/usr/bin/python3
"""Contains class BaseGeometry"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Class Recrangle: inherits from BaseGeometry"""
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
    
    def area(self):
        return self.__height * self.__width
    
    def __str__(self):
        return F"[Rectangle] {self.__width}/{self.__height}"
