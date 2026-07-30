#!/usr/bin/python3
"""This module defines a function that converts an object
to a JSON string"""


def to_json_string(my_obj):
    """Converts an object to a JSON string"""

    return json.dumps(my_obj)
