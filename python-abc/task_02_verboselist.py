#!/usr/bin/python3
"""
This module defines a class VerboseList that extends the built-in list class.
It provides notifications when items are added or removed.
"""


class VerboseList(list):
    """A list that prints messages when modified."""

    def append(self, item):
        """Adds an item and prints a message."""
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, items):
        """Extends the list and prints a message with the count."""
        count = len(items)
        super().extend(items)
        print("Extended the list with [{}] items.".format(count))

    def remove(self, item):
        """Prints a message and removes an item."""
        print("Removed [{}] from the list.".format(item))
        super().remove(item)

    def pop(self, index=-1):
        """Prints a message and pops an item."""
        item = self[index]
        print("Popped [{}] from the list.".format(item))
        return super().pop(index)
