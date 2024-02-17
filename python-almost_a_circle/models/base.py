#!/usr/bin/python3
"""This module defines a base class for future classes
 in this project."""

import json

class Base():
    """Defines a base class."""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes the class."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string representation"""

        if list_dictionaries is None or list_dictionaries == []:
            return("[]")
        if (type(list_dictionaries) is not list or
                not all(type(X) == dict for X in list_dictionaries)):
            return (json.dumps(list_dictionaries))
