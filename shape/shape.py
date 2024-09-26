""""
Description: A class to represent generic Shape objects.
Author: Bibekdeep Singh
Date: 25-09-24
""" 

from abc import ABC, abstractmethod

class Shape(ABC):
    """
    A class which represents shape objects.

    Attributes:
        color(str): Represents the color of the shape.

    Methods:
        calculate_area(): (Abstract) Calculates the area of the shape.
        calculate_perimeter(): (Abstract) Calculates the perimeter of the shape.
    """

    def __init__(self, color: str):

        """
        Initializes the class attribute color.

        Args:
            color(str): The color of the shape.
        
        Raises:
            ValueError: When the color is blank.
        
        """
        if len(color.strip()) == 0:
            raise ValueError("Color cannot be blank.")
        else:
            self._color = color

    def __str__(self) -> str:
        """
        String for color representation of the shape.

        Returns:
            str: Color of the shape.
        """
        return f"The shape color is {self._color}."
    
    @abstractmethod
    def calculate_area(self) -> float:
        """
        Abstract method: To be implemented in subclass.

        """
        pass

    @abstractmethod
    def calculate_perimeter(self) -> float:
        """
        Abstract method: To be implemented in subclass.
        """
        pass