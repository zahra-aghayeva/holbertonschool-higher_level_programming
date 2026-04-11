#!/usr/bin/python3
"""
This module defines a class MyList that inherits from the built-in list class.
It provides additional functionality to print the list in a sorted manner.
"""


class MyList(list):
    """
    MyList is a subclass of the built-in list class.
    It includes a method to print the elements of the list in ascending order.
    """

    def print_sorted(self):
        """
        Public instance method that prints the list, but sorted in ascending order.
        All elements in the list are assumed to be of type int.
        The original list remains unchanged after this method is called.
        """
        print(sorted(self))
