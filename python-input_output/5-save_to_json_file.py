#!/usr/bin/python3
"""This module defines a function that saves an object
to a JSON file"""
import json


def save_to_json_file(my_obj, fielname):
    """Writes an Object to a text file, using JSON
    representation"""

    with open(filename, "w", encoding="utf-8") as f:
        return json.dump(my_obj, f)
