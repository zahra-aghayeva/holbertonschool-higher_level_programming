#!/usr/bin/python3
"""
This module defines an abstract class Animal and its subclasses Dog and Cat.
"""
from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract class Animal."""

    @abstractmethod
    def sound(self):
        """Abstract method for sound."""
        pass


class Dog(Animal):
    """Subclass Dog that inherits from Animal."""

    def sound(self):
        """Implementation of sound for Dog."""
        return "Bark"


class Cat(Animal):
    """Subclass Cat that inherits from Animal."""

    def sound(self):
        """Implementation of sound for Cat."""
        return "Meow"
