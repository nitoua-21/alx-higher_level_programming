#!/usr/bin/python3
"""Unittest for the Base Class"""


import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import os


class TestBase(unittest.TestCase):
    """Test cases for Base class."""

    def setUp(self):
        """Set up test fixtures."""
        Base._Base__nb_objects = 0

    def test_base_instance(self):
        """Test Base instance."""
        b = Base()
        self.assertIsInstance(b, Base)

    def test_base_id(self):
        """Test Base id."""
        b1 = Base()
        b2 = Base()
        b3 = Base()
        b4 = Base(12)
        b5 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)
        self.assertEqual(b4.id, 12)
        self.assertEqual(b5.id, 4)

    def test_base_to_json_string(self):
        """Test Base to_json_string."""
        r = Rectangle(10, 7, 2, 8)
        dictionary = r.to_dictionary()
        json_string = Base.to_json_string([dictionary])
        self.assertIsInstance(json_string, str)

    def test_base_to_json_string_empty(self):
        """Test Base to_json_string empty."""
        json_string = Base.to_json_string([])
        self.assertEqual(json_string, "[]")

    def test_base_to_json_string_none(self):
        """Test Base to_json_string None."""
        json_string = Base.to_json_string(None)
        self.assertEqual(json_string, "[]")

    def test_base_from_json_string(self):
        """Test Base from_json_string."""
        list_input = [{'id': 89, 'width': 10, 'height': 4},
                      {'id': 7, 'width': 1, 'height': 7}]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Base.from_json_string(json_list_input)
        self.assertIsInstance(list_output, list)

    def test_base_from_json_string_empty(self):
        """Test Base from_json_string empty."""
        list_output = Base.from_json_string("[]")
        self.assertEqual(list_output, [])

    def test_base_from_json_string_none(self):
        """Test Base from_json_string None."""
        list_output = Base.from_json_string(None)
        self.assertEqual(list_output, [])

    def test_base_create_rectangle(self):
        """Test Base create rectangle."""
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertIsNot(r1, r2)
        self.assertNotEqual(r1, r2)

    def test_base_create_square(self):
        """Test Base create square."""
        s1 = Square(5)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertIsNot(s1, s2)
        self.assertNotEqual(s1, s2)

    def test_base_save_to_file_rectangle(self):
        """Test Base save_to_file rectangle."""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]
        Rectangle.save_to_file(list_rectangles_input)
        self.assertTrue(os.path.exists("Rectangle.json"))

    def test_base_save_to_file_square(self):
        """Test Base save_to_file square."""
        s1 = Square(5)
        s2 = Square(7, 9, 1)
        list_squares_input = [s1, s2]
        Square.save_to_file(list_squares_input)
        self.assertTrue(os.path.exists("Square.json"))

    def test_base_load_from_file_rectangle(self):
        """Test Base load_from_file rectangle."""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]
        Rectangle.save_to_file(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file()
        self.assertIsInstance(list_rectangles_output, list)
        self.assertEqual(len(list_rectangles_input),
                         len(list_rectangles_output))
        self.assertNotEqual(id(list_rectangles_input[0]), id(
            list_rectangles_output[0]))

    def test_base_load_from_file_square(self):
        """Test Base load_from_file square."""
        s1 = Square(5)
        s2 = Square(7, 9, 1)
        list_squares_input = [s1, s2]
        Square.save_to_file(list_squares_input)
        list_squares_output = Square.load_from_file()
        self.assertIsInstance(list_squares_output, list)
        self.assertEqual(len(list_squares_input), len(list_squares_output))
        self.assertNotEqual(
            id(list_squares_input[0]), id(list_squares_output[0]))

    def test_save_to_file_with_none(self):
        """check if Square.save_to_file(None) saves an empty list"""
        Square.save_to_file(None)
        with open("Square.json", "r") as file:
            content = file.read()
        self.assertEqual(content, "[]")

    def test_save_to_file_with_empty_list(self):
        """Check if Square.save_to_file([]) saves an empty list"""
        Square.save_to_file([])
        with open("Square.json", "r") as file:
            content = file.read()
        self.assertEqual(content, "[]")

    def test_save_to_file_with_single_square(self):
        """ Check if Square.save_to_file([Square(1)]) saves a single Square instance"""
        s = Square(1)
        Square.save_to_file([s])
        with open("Square.json", "r") as file:
            content = file.read()
        expected = '[{"id": 1, "size": 1, "x": 0, "y": 0}]'
        self.assertEqual(content, expected)


if __name__ == '__main__':
    unittest.main()
