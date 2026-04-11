#!/usr/bin/python3
"""
This module defines a class CountedIterator that extends the
functionality of a standard Python iterator by keeping track
of the number of items iterated.
"""


class CountedIterator:
    """An iterator that counts how many items have been fetched."""

    def __init__(self, iterable):
        """
        Initialize the iterator and the counter.

        Args:
            iterable: Any object that can be converted into an iterator.
        """
        self.iterator = iter(iterable)
        self.count = 0

    def get_count(self):
        """Returns the current number of items iterated."""
        return self.count

    def __next__(self):
        """
        Fetches the next item and increments the counter.
        Raises StopIteration if no items are left.
        """
        try:
            item = next(self.iterator)
            self.count += 1
            return item
        except StopIteration:
            raise StopIteration
