#!/usr/bin/python3
"""Unittest for class Square"""


import unittest
from models.rectangle import Rectangle
from models.square import Square


class TestSquare(unittest.TestCase):
    """Test cases for Square class."""

    def test_square_instance(self):
        """Test Square instance."""
        s = Square(5)
        self.assertIsInstance(s, Square)
        self.assertIsInstance(s, Rectangle)

    def test_square_size(self):
        """Test Square size."""
        s1 = Square(5)
        self.assertEqual(s1.size, 5)
        s2 = Square(5, 4)
        self.assertEqual(s2.size, 5)
        s2 = Square(5, 4)
        self.assertEqual(s2.x, 4)

    def test_invalid_size_type(self):
        """Test invalid size type."""
        with self.assertRaises(TypeError) as context:
            s = Square("5", 4)
        with self.assertRaises(TypeError) as context:
            s = Square("5")
        with self.assertRaises(TypeError) as context:
            s = Square(2.5, 4)
        self.assertEqual(str(context.exception), "width must be an integer")
        with self.assertRaises(TypeError) as context:
            s = Square([1, 2], 4)
        self.assertEqual(str(context.exception), "width must be an integer")
        with self.assertRaises(TypeError) as context:
            s = Square({"size": 10}, 4)
        self.assertEqual(str(context.exception), "width must be an integer")
        with self.assertRaises(TypeError) as context:
            s = Square((4,), 4)
        self.assertEqual(str(context.exception), "width must be an integer")
        with self.assertRaises(TypeError) as context:
            s = Square(None, 4)
        self.assertEqual(str(context.exception), "width must be an integer")

    def test_size_zero_or_negative(self):
        """Test width is zero or negative."""
        with self.assertRaises(ValueError) as context:
            r = Square(0)
        self.assertEqual(str(context.exception), "width must be > 0")
        with self.assertRaises(ValueError) as context:
            r = Square(-1, 4)
        self.assertEqual(str(context.exception), "width must be > 0")
        with self.assertRaises(ValueError) as context:
            r = Square(-1)
        self.assertEqual(str(context.exception), "width must be > 0")

    def test_square_x(self):
        """Test Square x."""
        s = Square(5, 2, 3)
        self.assertEqual(s.x, 2)

    def test_invalid_x_type(self):
        """Test invalid x type."""
        with self.assertRaises(ValueError) as context:
            s = Square(1, -2)
        self.assertEqual(str(context.exception), "x must be >= 0")
        with self.assertRaises(TypeError) as context:
            s = Square(1, "3")
        self.assertEqual(str(context.exception), "x must be an integer")

    def test_square_y(self):
        """Test Square y."""
        s = Square(5, 2, 3)
        self.assertEqual(s.y, 3)
        with self.assertRaises(ValueError) as context:
            s = Square(1, 2, -1)
        self.assertEqual(str(context.exception), "y must be >= 0")
        with self.assertRaises(TypeError) as context:
            s = Square(1, 2, "3")
        self.assertEqual(str(context.exception), "y must be an integer")

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
        s = Square(5, 2, 3, 10)
        expected = {'id': 10, 'size': 5, 'x': 2, 'y': 3}
        self.assertEqual(s.to_dictionary(), expected)


if __name__ == '__main__':
    unittest.main()
