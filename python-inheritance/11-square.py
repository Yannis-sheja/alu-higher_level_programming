#!/usr/bin/python3
"""This module defines a square that inherits from Rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represents a square"""

    def __init__(self, size):
        """Initialize the new square"""

        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """Return the printable representation of the square"""

        return "[Square] {}/{}".format(self.__size, self.__size)
