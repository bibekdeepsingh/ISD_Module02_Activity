"""
Description: Unit tests for the Rectangle class.
Author: {Student Name}
Date: {Date}
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests/shape/rectangle.py
"""
import math
import unittest
from shape.rectangle import Rectangle

class TestRectangle(unittest.TestCase):

    def test_valid_rectangle(self):
        rectangle = Rectangle("green", 5, 6)
        self.assertEqual(rectangle.calculate_area(), 30)
        self.assertEqual(rectangle.calculate_perimeter(), 22)
        self.assertEqual(str(rectangle), "The shape color is green\nThis rectangle has four sides with the lengths of 5, 6, 5 and 6 centimeters.")

    def test_invalid_length(self):
        with self.assertRaises(ValueError) as context:
            Rectangle("green", "not_a_number", 6)
        self.assertEqual(str(context.exception), "Length must be numeric.")

    def test_invalid_width(self):
        with self.assertRaises(ValueError) as context:
            Rectangle("green", 5, "not_a_number")
        self.assertEqual(str(context.exception), "Width must be numeric.")

    def test_blank_color(self):
        with self.assertRaises(ValueError) as context:
            Rectangle("", 5, 6)
        self.assertEqual(str(context.exception), "Color cannot be blank.")

if __name__ == "__main__":
    unittest.main()
