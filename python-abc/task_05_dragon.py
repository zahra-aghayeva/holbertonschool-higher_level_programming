#!/usr/bin/python3
"""
This module demonstrates the use of mixins to compose behaviors
in a Dragon class.
"""


class SwimMixin:
    """Mixin to add swimming behavior."""

    def swim(self):
        """Prints swimming message."""
        print("The creature swims!")


class FlyMixin:
    """Mixin to add flying behavior."""

    def fly(self):
        """Prints flying message."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """
    Dragon class that inherits swimming and flying abilities from mixins.
    """

    def roar(self):
        """Prints a roaring message unique to the dragon."""
        print("The dragon roars!")
