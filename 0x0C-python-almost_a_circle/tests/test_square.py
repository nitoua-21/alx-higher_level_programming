#!/usr/bin/python3
"""Unittest for class Square"""


import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """Test cases for Square class."""

    def test_square_instance(self):
        """Test Square instance."""
        s = Square(5)
        self.assertIsInstance(s, Square)

    def test_square_size(self):
        """Test Square size."""
        s = Square(5)
        self.assertEqual(s.size, 5)

    def test_square_x(self):
        """Test Square x."""
        s = Square(5, 2, 3)
        self.assertEqual(s.x, 2)

    def test_square_y(self):
        """Test Square y."""
        s = Square(5, 2, 3)
        self.assertEqual(s.y, 3)

    def test_square_area(self):
        """Test Square area."""
        s = Square(5)
        self.assertEqual(s.area(), 25)

    def test_square_display(self):
        """Test Square display."""
        s = Square(4)
        s.display()

    def test_square_str(self):
        """Test Square str."""
        s = Square(4, 2, 1, 12)
        self.assertEqual(str(s), "[Square] (12) 2/1 - 4")

    def test_square_update_args(self):
        """Test Square update with args."""
        s = Square(10, 10, 10)
        s.update(89)
        self.assertEqual(s.id, 89)

    def test_square_update_kwargs(self):
        """Test Square update with kwargs."""
        s = Square(10, 10, 10)
        s.update(size=5, x=2)
        self.assertEqual(s.size, 5)
        self.assertEqual(s.x, 2)

    def test_square_to_dictionary(self):
        """Test Square to_dictionary."""
        s = Square(5, 2, 1)
        dictionary = s.to_dictionary()
        self.assertIsInstance(dictionary, dict)


if __name__ == '__main__':
    unittest.main()
