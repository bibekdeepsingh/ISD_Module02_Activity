"""
Description: Unit tests for the Rectangle class.
Author: Bibekdeep Singh
Date: 27-09-24
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests/shape/rectangle.py
"""
import math
import unittest
from shape.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    
    def setUp(self):
        self.rectangle = Rectangle("green", 6,2)

        
    """def test_init_valid_inputs_attributes_set(self):
        #Arrange and act
        rectangle = Rectangle("green", 6,2)

        #assert
        self.assertEqual(rectangle._color , "green")
        self.assertEqual(rectangle.__length , 6)
        self.assertEqual(rectangle.__width , 2)"""

    def test_init_invalid_color_valueerror(self):
        #act and assert
        with self.assertRaises(ValueError):
            rectangle = Rectangle("", 6, 2)

    def test_init_invalid_length_valueerror(self):
        #act and assert
        with self.assertRaises(ValueError):
            rectangle = Rectangle("green", "six", 2)
       

    def test_init_invalid_width_valueerror(self):
        #act and assert
        with self.assertRaises(ValueError):
            rectangle = Rectangle("green", 6, "two")

    def test_init_returns_calculated_area(self):
        #act and assert
        rectangle = Rectangle("green",6, 2)
        self.assertEqual(rectangle.calculate_area(), 12)

    def test_init_returns_calculated_perimeter(self):
        #act and assert
        rectangle = Rectangle("green",6, 2)
        self.assertEqual(rectangle.calculate_perimeter(), 16)

    

if __name__ == "__main__":
    unittest.main()
