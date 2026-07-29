#!/usr/bin/python3
"""This module defines a function that returns true
if obj is instance or inherited from"""


def is_kind_of_class(obj, a_class):
    """Return True if obj is an instance of a_class or sub_class"""

    return isinstance(obj, a_class)
