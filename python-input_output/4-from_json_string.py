#!/usr/bin/python3
"""This module defines a function that converts a JSON string
into an object"""
import json


def from_json_string(my_str):
    """Converts a JSON string into an object"""

    return json.loads(my_str)
