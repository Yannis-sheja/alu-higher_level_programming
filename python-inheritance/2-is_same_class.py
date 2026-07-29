#!/usr/bin/python3
"""This module defines a functions that check exact class match"""


def is_same_class(obj, a_class):
    """return True if obj is exactly an instance of a_class"""

    return type(obj) is a_class
