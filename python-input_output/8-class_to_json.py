#!/usr/bin/python3
"""This module defines a function that serialize the
attributes of an object"""


def class_to_json(obj):
    """Returns the dictionary description for JSON serialization
    ofan object"""

    return obj.__dict__
