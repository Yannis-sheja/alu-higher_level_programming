#!/usr/bin/python3
"""This module defines a function that check
the strict inheritance"""


def inherits_from(obj, a_class):
    """Return True if the object is an instance of
    a class inherited"""

    return isinstance(obj, a_class) and type(obj) is not a_class
