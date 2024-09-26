""""
Description: A class to represent Triangle objects.
Author: Bibekdeep Singh
Date: 26-09-2024
"""

from shape.shape import Shape
import math

class Triangle(Shape):
    """
    Traingle: Class to represent Triangle shape.

    Attributes:
        Inherited attributes from courses class.
        __side_1(int): Side 1 of the triangle.
        __side_2(int): Side 2 of the triangle.
        __side_3(int): Side 3 of the triangle.

    Methods:
        Inherited methods from shape class.
        __init__(): Initializes triangle class instance.
        __str__(): Returns a string representation of triangle class.
    """

    def __init__(self, color:str, side_1:int, side_2:int, side_3:int):
        """
        Initializes the triangle class with color and three sides.

        Args:
            inherited from shape class.
            __side_1(int): Length of the first side of the triangle.
            __side_2(int): Length of the second side of the triangle
            __side_3(int): Length of the third side of the triangle.

        Raises:
            ValueError:
                When Side 1 is not numeric.
                When Side 2 is not numeric.
                When Side 3 is not numeric.
        """

        super().__init__(color)

        if not isinstance(side_1, int):
            raise ValueError("Side 1 must be numeric.")
        
        else: 
            self.__side_1 = side_1

        if not isinstance(side_2, int):
            raise ValueError("Side 2 must be numeric.")
        
        else:
            self.__side_2 = side_2

        if not isinstance(side_3, int):
            raise ValueError("Side 3 must be numeric.")
        
        else:
            self.__side_3 = side_3
        
    def __str__(self) -> str:
        """
        Returns a string representation of Triangle class.

        Returns:
            str: The triangle object as a string.
        """
        
        value = super().__str__()
        value += f"This triangle has three sides with lengths of {self.__side_1}, {self.__side_2} and {self.__side_3} centimeters."
        return value
        
    def calculate_area(self) -> float:
        """
        Calculate and then returns the area of the traingle.

        Returns:
            float: area of the triangle.
        """

        semi_perimeter = (self.__side_1 + self.__side_2 + self.__side_3) / 2
        area = math.sqrt(semi_perimeter * (semi_perimeter - self.__side_1) * (semi_perimeter - self.__side_2) * (semi_perimeter - self.__side_3))
        return area
    
    def calculate_perimeter(self) -> float:
        """
        Calculates the perimeter of the triangle.

        Returns:
            float: Perimeter of the triangle.
        """

        perimeter = self.__side_1 + self.__side_2 + self.__side_3
        return perimeter

