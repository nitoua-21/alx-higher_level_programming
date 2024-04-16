#!/usr/bin/python3
"""Module contains a class Student that defines a studen"""


class Student:
    """Defines a student"""

    def __init__(self, first_name, last_name, age):
        """Instantiates a Student with first_name, last_name, and age"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieves a dictionary representation of a Student instance"""
        return self.__dict__
