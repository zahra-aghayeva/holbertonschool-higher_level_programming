#!/usr/bin/python3
"""
This module defines an abstract class Shape and its subclasses
Circle and Rectangle, demonstrating duck typing.
"""
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract class for shapes."""

    @abstractmethod
    def area(self):
        """Calculates the area of the shape."""
        pass

    @abstractmethod
    def perimeter(self):
        """Calculates the perimeter of the shape."""
        pass


class Circle(Shape):
    """Concrete class Circle."""

    def __init__(self, radius):
        """Initialize Circle with radius."""
        self.radius = radius

    def area(self):
        """Return the area of the circle."""
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """Return the perimeter of the circle."""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Concrete class Rectangle."""

    def __init__(self, width, height):
        """Initialize Rectangle with width and height."""
        self.width = width
        self.height = height

    def area(self):
        """Return the area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Return the perimeter of the rectangle."""
        return 2 * (self.width + self.height)


def shape_info(obj):
    """
    Prints the area and perimeter of a shape using duck typing.
    It doesn't check if obj is an instance of Shape, just calls the methods.
    """
    print("Area: {}".format(obj.area()))
    print("Perimeter: {}".format(obj.perimeter()))
