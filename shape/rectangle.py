""""
Description: A class to represent Rectangle objects.
Author: Bibekdeep Singh
Date: 26-09-24
"""
from shape.shape import Shape

class Rectangle(Shape):
    """
    Rectangle class.

    Attributes:
        Inherited attributes from shapes class.
        __length(int): Represents the length of rectangle.
        __width(int): Represents the width of rectangle.

    Methods: 
        Inherited methods from shapes class.
        __init__(): Initializes rectangle class instance.
        __str__(): Returns a string representation of rectangle class.
    """ 

    def __init__(self, color:str, length:int , width:int):
        """
        Initializes the rectangle class object.

        Args:
            color(str): The color of the shape.
            length(int): The length of rectangle.
            width(int): The width of rectangle.
            
        Raises:
            ValueError:
                When length is not numeric.
                When Width is not numeric.
        """
        super().__init__(color)

        if not isinstance(length, int):
            raise ValueError("Length must be numeric.")
        if not isinstance(width, int):
            raise ValueError("Width must be numeric.")
        
        self.__length = length
        self.__width = width

    def __str__(self) -> str:
        """
        Return a string representation of rectangle class.

        Returns:
            str: The rectangle object as a string.
        """
        value = super().__str__()
        value += f"This rectangle has four sides with the lengths of {self.__length}, {self.__width}, {self.__length} and {self.__width} centrimeter."
        return value
    
    def calculate_area(self) -> float:
        """
        Calculates the area of rectangle.

        Returns:
            float: The area of rectangle.
        
        """
        return self.__length * self.__width
    
    def calculate_perimeter(self) -> float:
        """
        Calculates the area of rectangle.

        Returns:
            float: The perimeter of rectangle.
0        """
        return 2*{self.__length} + 2*{self.__width}

        

        