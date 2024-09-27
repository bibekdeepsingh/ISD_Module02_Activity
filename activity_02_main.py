""""
Description: A client program written to verify correctness of 
the activity classes.
Author: ACE Faculty
Edited by: Bibekdeep Singh
Date: 27-09-24
"""


from shape.shape import *
from shape.triangle import Triangle
from shape.rectangle import Rectangle

def main():
    """Test the functionality of the methods encapsulated 
    in this project.
    """ 
    # In the statements coded below, ensure that any statement that could result 
    # in an exception is handled.  When exceptions are 'caught', display the exception 
    # message to the console.

    # *** PART 1 ***
    print("*************PART 1****************")
    # 1. Create an empty list of Shape objects.
    shapes = []

    # 2. Code a statement which creates an instance of the Triangle class.
    # Append the Triangle to the list of shapes.
    try:
        triangle = Triangle("blue", 3, 4, 5)
        shapes.append(triangle)
    except ValueError as e:
        print(f"Error creating triangle: {e}")


    # 3. Code a statement which creates an instance of the Rectangle class.
    # Append the Rectangle to the list of shapes.
    try:
        rectangle = Rectangle("green", 6, 2)
        shapes.append(rectangle)
    except ValueError as e:
        print(f"Error creating rectangle: {e}")



    # 4. Code 3 additional statements which creates an instance of 
    # Triangle or Rectangle classes (your choice).
    # Append these instances to the list of shapes.
    try:
        triangle1 = Triangle("red", 7, 8, 9)
        shapes.append(triangle1)
    except ValueError as e:
        print(f"Error creating triangle1: {e}")

    try:
        rectangle1 = Rectangle("yellow", 4, 3)
        shapes.append(rectangle1)
    except ValueError as e:
        print(f"Error creating rectangle1: {e}")

    try:
        triangle2 = Triangle("purple", 6, 6, 6)
        shapes.append(triangle2)
    except ValueError as e:
        print(f"Error creating triangle2: {e}")


    # 5. Iterate through the list of shapes.  On each iteration:
    # - print the shape
    # - print the area of the shape to 2 decimal places
    # - print the perimeter of the shape to 2 decimal places
    for shape in shapes:
        try:
            print(shape)
            print(f"Area: {shape.calculate_area():.2f}")
            print(f"Perimeter: {shape.calculate_perimeter():.2f}")
            print("------------------------------")
        except Exception as e:
            print(f"Error processing shape {shape}: {e}")


    # *** END PART 1 ***

    # *** PART 2 ***
    print("*************PART 2****************")
    # 1. Create an empty list of Vehicle objects.


    # 2. Code a statement which creates an instance of the Automobile class.
    # Append the Automobile to the list of vehicles.



    # 3. Code a statement which creates an instance of the Aircraft class.
    # Append the Aircraft to the list of vehicles.



    # 4. Code 3 additional statements which creates an instance of 
    # Automobile, Aircraft or Train classes (your choice).
    # Append these instances to the list of vehicles.




    # 5. Iterate through the list of vehicles.  On each iteration:
    # - print the vehicle
    # - print the phrase:
    # "Fuel needed for 500 kilometers: {fuel requirements} litres."



if __name__ == "__main__":
    main()