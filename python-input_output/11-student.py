#!/usr/bin/python3
"""This module defines a student class"""


class Student:
    """Represents a student"""

    def __init__(self, first_name, last_name, age):
        """Initialise a new student"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation"""

        if type(attrs) is list and all(type(a) is str for a in attrs):
            return {k: v for k, v in self.__dict__.items() if k in attrs}

        return self.__dict__

    def reload_from_json(self, json):
        """Replaces all attributes of the Student from a dictionary"""

        for key, value in json.items():
            setattr(self, key, value)
