#!/usr/bin/python3
"""Unittest for the Rectangle class"""


import unittest
from models.rectangle import Rectangle, Base


class TestRectangle(unittest.TestCase):
    """Test cases for Rectangle class."""

    def setUp(self):
        """Set up test fixtures."""
        Base._Base__nb_objects = 0

    def test_rectangle_instance(self):
        """Test Rectangle instance."""
        r = Rectangle(10, 7, 2, 8)
        self.assertIsInstance(r, Rectangle)
        self.assertIsInstance(r, Base)

    def test_rectangle_id(self):
        """Test Rectangle id."""
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r2.id, 2)
        self.assertEqual(r3.id, 12)

    def test_rectangle_width(self):
        """Test Rectangle width."""
        r = Rectangle(10, 7, 2, 8)
        self.assertEqual(r.width, 10)

    def test_invalid_width_type(self):
        """Test invalid width type."""
        with self.assertRaises(TypeError) as context:
            r = Rectangle("5", 4)
        with self.assertRaises(TypeError) as context:
            r = Rectangle(2.5, 4)
        self.assertEqual(str(context.exception), "width must be an integer")
        with self.assertRaises(TypeError) as context:
            r = Rectangle([1, 2], 4)
        self.assertEqual(str(context.exception), "width must be an integer")
        with self.assertRaises(TypeError) as context:
            r = Rectangle({"width": 10}, 4)
        self.assertEqual(str(context.exception), "width must be an integer")
        with self.assertRaises(TypeError) as context:
            r = Rectangle((4,), 4)
        self.assertEqual(str(context.exception), "width must be an integer")
        with self.assertRaises(TypeError) as context:
            r = Rectangle(None, 4)
        self.assertEqual(str(context.exception), "width must be an integer")

    def test_width_zero_or_negative(self):
        """Test width is zero or negative."""
        with self.assertRaises(ValueError) as context:
            r = Rectangle(0, 4)
        self.assertEqual(str(context.exception), "width must be > 0")
        with self.assertRaises(ValueError) as context:
            r = Rectangle(-1, 4)
        self.assertEqual(str(context.exception), "width must be > 0")

    def test_rectangle_height(self):
        """Test Rectangle height."""
        r = Rectangle(10, 7, 2, 8)
        self.assertEqual(r.height, 7)

    def test_invalid_height_type(self):
        """Test invalid height type."""
        with self.assertRaises(TypeError) as context:
            r = Rectangle(5, "4")
        with self.assertRaises(TypeError) as context:
            r = Rectangle(4, 2.5)
        self.assertEqual(str(context.exception), "height must be an integer")
        with self.assertRaises(TypeError) as context:
            r = Rectangle(4, [1, 2])
        self.assertEqual(str(context.exception), "height must be an integer")
        with self.assertRaises(TypeError) as context:
            r = Rectangle(4, {"height": 10})
        self.assertEqual(str(context.exception), "height must be an integer")
        with self.assertRaises(TypeError) as context:
            r = Rectangle(4, (4,))
        self.assertEqual(str(context.exception), "height must be an integer")
        with self.assertRaises(TypeError) as context:
            r = Rectangle(4, None)
        self.assertEqual(str(context.exception), "height must be an integer")

    def test_height_zero_or_negative(self):
        """Test height is zero or negative."""
        with self.assertRaises(ValueError) as context:
            r = Rectangle(4, 0)
        self.assertEqual(str(context.exception), "height must be > 0")
        with self.assertRaises(ValueError) as context:
            r = Rectangle(4, -4)
        self.assertEqual(str(context.exception), "height must be > 0")

    def test_rectangle_x(self):
        """Test Rectangle x."""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(10, 7)
        r3 = Rectangle(10, 7, 0)
        self.assertEqual(r1.x, 2)
        self.assertEqual(r2.x, 0)
        self.assertEqual(r3.x, 0)

    def test_invalid_x_type(self):
        """Test invalid x type."""
        with self.assertRaises(TypeError) as context:
            r = Rectangle(5, 4, "2")
        with self.assertRaises(TypeError) as context:
            r = Rectangle(5, 4, 2.5)
        self.assertEqual(str(context.exception), "x must be an integer")
        with self.assertRaises(TypeError) as context:
            r = Rectangle(5, 4, [1, 2])
        self.assertEqual(str(context.exception), "x must be an integer")
        with self.assertRaises(TypeError) as context:
            r = Rectangle(5, 4, {"x": 2})
        self.assertEqual(str(context.exception), "x must be an integer")
        with self.assertRaises(TypeError) as context:
            r = Rectangle(5, 4, (2,))
        self.assertEqual(str(context.exception), "x must be an integer")
        with self.assertRaises(TypeError) as context:
            r = Rectangle(5, 4, None)
        self.assertEqual(str(context.exception), "x must be an integer")

    def test_x_negative(self):
        """Test x is negative."""
        with self.assertRaises(ValueError) as context:
            r = Rectangle(5, 4, -2)
        self.assertEqual(str(context.exception), "x must be >= 0")

    def test_rectangle_y(self):
        """Test Rectangle y."""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(10, 7)
        r3 = Rectangle(10, 7, 5, 0)
        self.assertEqual(r1.y, 8)
        self.assertEqual(r2.y, 0)
        self.assertEqual(r3.y, 0)

    def test_invalid_y_type(self):
        """Test invalid y type."""
        with self.assertRaises(TypeError) as context:
            r = Rectangle(5, 4, 3, "2")
        with self.assertRaises(TypeError) as context:
            r = Rectangle(5, 4, 3, 3.5)
        self.assertEqual(str(context.exception), "y must be an integer")
        with self.assertRaises(TypeError) as context:
            r = Rectangle(5, 4, 4, [1, 2])
        self.assertEqual(str(context.exception), "y must be an integer")
        with self.assertRaises(TypeError) as context:
            r = Rectangle(5, 4, 3, {"y": 2})
        self.assertEqual(str(context.exception), "y must be an integer")
        with self.assertRaises(TypeError) as context:
            r = Rectangle(5, 4, 1, (2,))
        self.assertEqual(str(context.exception), "y must be an integer")
        with self.assertRaises(TypeError) as context:
            r = Rectangle(5, 4, 10, None)
        self.assertEqual(str(context.exception), "y must be an integer")

    def test_y_negative(self):
        """Test y is negative."""
        with self.assertRaises(ValueError) as context:
            r = Rectangle(5, 4, 5, -2)
        self.assertEqual(str(context.exception), "y must be >= 0")

    def test_rectangle_area(self):
        """Test Rectangle area."""
        r = Rectangle(10, 7, 2, 8)
        self.assertEqual(r.area(), 70)

    def test_rectangle_display(self):
        """Test Rectangle display."""
        r = Rectangle(4, 6)
        r.display()

    def test_rectangle_str(self):
        """Test Rectangle str."""
        r = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r), "[Rectangle] (12) 2/1 - 4/6")

    def test_rectangle_update_args(self):
        """Test Rectangle update with args."""
        r = Rectangle(10, 10, 10, 10)
        r.update(89)
        self.assertEqual(r.id, 89)

    def test_rectangle_update_kwargs(self):
        """Test Rectangle update with kwargs."""
        r = Rectangle(10, 10, 10, 10)
        r.update(width=1, x=2)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.x, 2)

    def test_rectangle_to_dictionary(self):
        """Test Rectangle to_dictionary."""
        r = Rectangle(10, 7, 2, 8)
        dictionary = r.to_dictionary()
        self.assertIsInstance(dictionary, dict)


if __name__ == '__main__':
    unittest.main()
