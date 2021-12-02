# Ozan Yetkin | 1908227
# %%
# Importing necessary modules
from math import pi, sqrt

# Defining the class for circle
class Circle:

    # Initializing the class with radius, defaulting to one
    def __init__(self, radius=1):

        # Calculating and setting the radius, diameter, and area
        self._radius = radius
        self._diameter = radius * 2
        self._area = pi * radius ** 2

    # Making a nice string representation for circle class
    def __str__(self):
        return f"Circle({self._radius})"

    # Defining its representation to print custom string on console
    def __repr__(self):
        return str(self)

    # Defining the radius method, with default radius as None
    def radius(self, radius=None):
        # If radius is provided by the user, updating the radius, along with diameter and area
        if radius is not None:
            self._radius = radius
            self._diameter = radius * 2
            self._area = pi * radius ** 2
        # If radius is not provided by the user, just returning the current radius
        return self._radius

    # Defining the diameter method, with default diameter as None
    def diameter(self, diameter=None):
        # If diameter is provided by the user, updating the diameter, along with radius and area
        if diameter is not None:
            self._radius = diameter / 2
            self._diameter = diameter
            self._area = pi * (diameter / 2) ** 2
        # If diameter is not provided, just returning the current diameter
        return self._diameter

    # Same goes for defining the area method
    def area(self, area=None):
        # If area is given, updating all attributes accordingly
        if area is not None:
            self._radius = sqrt(area / pi)
            self._diameter = sqrt(area / pi) * 2
            self._area = area
        # If area is not given, returning the current
        return self._area


# Test Cases
# %%

c = Circle(5)
print(c.radius())
print(c.diameter())
print(c.area())

# %%

c = Circle()
print(c.radius())
print(c.diameter())

# %%

c = Circle()
print(c.radius())
print(c.area())

c.area(10)
print(c.area())

# %%

c = Circle(2)
c.radius(1)
print(c.diameter())
print(c.area())

c.radius(2)
print(c.diameter())
print(c.area())

c.area(5)
print(c.radius())
print(c.diameter())

# %%
