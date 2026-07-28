#!/usr/bin/python3
"""This module calculate the area of the square"""


class Square:
    """ Initialize a square"""

    def __init__(self, size=0):
        """TypeError and ValueError using raise command"""

        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """Returns tha area of the square(Size*size)"""
        return self.__size * self.__size
