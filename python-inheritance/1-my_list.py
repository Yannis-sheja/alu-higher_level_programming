#!/usr/bin/python3
"""This module defines a list with the sorted method"""


class Mylist(list):
    """Represents a list that can print itself sorted"""

    def print_sorted(self):
        """Prints the list in ascending order"""

        print(sorted(self))
