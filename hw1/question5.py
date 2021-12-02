# Ozan Yetkin | 1908227
# %%
# Importing necessary packages
import math


# Provided base class for Triangle, Parallelogram, IsoscelesTriangle, EquilateralTriangle, Rectangle, and Square
class Polygon:
    def __init__(self, sides):
        """Initialized with the lengths of the sides"""
        for s in sides:
            if s <= 0:
                raise ValueError("Side lengths must be positive")
        self._sides = sides
        self._name = "Polygon"

    def name(self):
        return self._name

    def area(self):
        """The area of an arbitrary polygon is unknown"""
        # Try to get the area of a Polygon
        try:
            # If the get_area method is present, it means that we can call and store its value in area
            area = self.get_area()

        # If the method is not present, it would cause an AttributeError which needs an exception
        except AttributeError:
            # If AttributeError raises, create a new object which overrides __format__ function and store it in area
            area = UnknownArea()

        # After handling exception, return the area for all polygons regardless of having the get_area method or not
        return area

    def perimeter(self):
        total = 0.0
        for s in self._sides:
            total += s
        return total


# %%
# Create class for Triangle that inherits attributes from Polygon which will encapsulate IsoscelesTriangle and EquilateralTriangle
class Triangle(Polygon):

    # Initialize the class with 4 arguments, 3 for individual sides, 1 for all sides (which is a must because of inheritance of Polygon)
    def __init__(self, side_1, side_2=None, side_3=None, sides=None):
        # Use individual sides to make it a single list that contains all sides
        sides = [side_1, side_2, side_3]
        # Initialize it with inheriting from Polygon class, which only needs sides as a single list
        super().__init__(sides)
        # Change the name attribute to Triangle to separate it from Polygon
        self._name = "Triangle"

    # Define a method to calculate the area of a triangle using Heron's formula
    def get_area(self):
        # Calculate the half of the perimeter and store it in a variable
        semi_perimeter = self.perimeter() / 2

        # Initialize a new variable called s and iterate over sides of triangle
        s = 1
        for side in self._sides:
            # Calculate s = (semi_perimeter - side[0]) * (semi_perimeter - side[1]) * (semi_perimeter - side[2])
            s *= semi_perimeter - side

        # Calculate and return the final area by calculating the square root of semi_perimeter * s
        area = math.sqrt(semi_perimeter * s)
        return area


# Create class for IsoscelesTriangle that inherits from Triangle class
class IsoscelesTriangle(Triangle):

    # Define it with using 3 individual sides and a list containing all sides for inheritance purposes
    def __init__(self, side_1, side_2=None, side_3=None, sides=None):

        # Initialize it using side_3 being equal to side_1, and sides list containing all individual side lengths
        super().__init__(side_1, side_2=side_2, side_3=side_1, sides=sides)
        # Concatenate "Isosceles" prefix to Triangle as its name
        self._name = "Isosceles " + self._name


# Create class for IsoscelesTriangle that inherits from Triangle class
class EquilateralTriangle(Triangle):

    # Define it with using 3 individual sides and a list containing all sides for inheritance purposes
    def __init__(self, side_1, side_2=None, side_3=None, sides=None):

        # Initialize it using side_2 and side_3 being equal to side_1, and sides list containing all individual side lengths
        super().__init__(side_1, side_2=side_1, side_3=side_1, sides=sides)
        # Concatenate "Equilateral" prefix to Triangle as its name
        self._name = "Equilateral " + self._name


# %%
# Create class for Parallelogram that inherits attributes from Polygon which will encapsulate Rectangle and Square
class Parallelogram(Polygon):

    # Initialize the class with 3 arguments, 2 for individual sides, 1 for all sides (which is a must because of inheritance of Polygon)
    def __init__(self, side_1, side_2=None, sides=None):

        # Use individual sides to make it a single list that contains all sides
        sides = [side_1, side_2] * 2
        super().__init__(sides)

    # Define a method to calculate the area of a parallelogram (which only works with right angles, but it is enough for rectangle and square)
    def get_area(self):
        # Calculate the area by multiplying its two sides, it is safe to reach them by index since sides list defined as [side_1, side_2] * 2
        area = self._sides[0] * self._sides[1]
        return area


# Create class for Rectangle that inherits from Parallelogram class
class Rectangle(Parallelogram):

    # Define it with using 2 individual sides and a list containing all sides for inheritance purposes
    def __init__(self, side_1, side_2=None, sides=None):
        super().__init__(side_1, side_2, sides=sides)
        # Change the name attribute to "Rectangle"
        self._name = "Rectangle"


# Create class for Square that inherits from Parallelogram class
class Square(Parallelogram):

    # Define it with using 2 individual sides and a list containing all sides for inheritance purposes
    def __init__(self, side_1, side_2=None, sides=None):
        # Initialize it using side_2 being equal to side_1, and sides list containing all individual side lengths
        super().__init__(side_1, side_2=side_1, sides=sides)
        # Change the name attribute to "Square"
        self._name = "Square"


# %%
# Create a simple class to override __format__ method for an unknown area, since {1:.3f} in the test case would only work for an int or float
class UnknownArea:

    # Initialize the class and just pass since we don't need any attribute at all
    def __init__(self):
        pass

    # Override the __format__ method and just return a blank string
    def __format__(self, format_spec):
        return " "


# Test case including Polygon, Triangle, Parallelogram, IsoscelesTriangle, EquilateralTriangle, Rectangle, and Square
shapelist = [
    Polygon([1.0, 4.5, 3.1, 3.3]),
    Triangle(3.4, 5.3, 4.2),
    IsoscelesTriangle(4.1, 1),
    EquilateralTriangle(4.2),
    Rectangle(5, 4),
    Square(3.25),
]

for shape in shapelist:
    print(
        "{0} Area: {1:.3f}  Perimeter: {2:.3f}".format(
            shape.name(), shape.area(), shape.perimeter()
        )
    )
