#!/usr/bin/python3
"""Kvadrat sinifini təyin edən modul."""


class Square:
    """Kvadratı təmsil edən sinif."""

    def __init__(self, size):
        """Kvadrat obyekti yaradılır.

        Args:
            size: Kvadratın tərəfinin ölçüsü.
        """
        self.__size = size
