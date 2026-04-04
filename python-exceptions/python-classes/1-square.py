#!/usr/bin/python3
"""Kvadrat sinifini təyin edən modul."""


class Square:
    """Kvadratı təmsil edən sinif."""

    def __init__(self, size):
        """Kvadratı müəyyən ölçü ilə başladır.

        Args:
            size (int): Kvadratın tərəfinin ölçüsü.
        """
        self.__size = size
