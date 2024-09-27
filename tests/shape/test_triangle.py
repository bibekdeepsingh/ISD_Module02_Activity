"""
Description: Unit tests for the Book class.
Author: Bibekdeep Singh
Date: 26-09-24
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests/shape/test_triangle.py
"""

import unittest
from shape.triangle import Triangle

class TestTriangle(unittest.TestCase):

    def setUp(self):
        self.triangle = Triangle("blue", 3, 4, 5)

    """ def test_init_valid_inputs_attributes_set(self):
        triangle = Triangle("blue", 3, 4, 5)
        self.assertEqual(triangle._color, "blue")
        self.assertEqual(triangle.__side_1, 3)
        self.assertEqual(triangle.__side_2, 4)
        self.assertEqual(triangle.__side_3, 5) """

    def test_init_invalid_color_Valueerror(self):
        #act and assert
        with self.assertRaises(ValueError):
            triangle = Triangle("", 3, 4, 5)

    def test_init_invalid_side_1_valueerror(self):
        #act and assert
        with self.assertRaises(ValueError):
            triangle = Triangle("blue", "three", 4, 5)
      
    def test_init_invalid_side_2_valuerror(self):
        #act and assert
        with self.assertRaises(ValueError):
            triangle = Triangle("blue", 3, "four", 5)

    def test_init_invalid_side_3_valueerror(self):
        #act and assert
        with self.assertRaises(ValueError):
            triangle = Triangle("blue", 3, 4, "five")
    
    def test_init_returns_calculated_area(self):
        #act and assert
        triangle = Triangle("blue",3, 4, 5)
        self.assertEqual(triangle.calculate_area(), 6.0)

    def test_init_returns_calculated_perimeter(self):
        #act and assert
        triangle = Triangle("blue",3 , 4, 5)
        self.assertEqual(triangle.calculate_perimeter(), 12)
 

if __name__ == "__main__":
    unittest.main()
