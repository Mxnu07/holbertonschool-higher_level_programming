#!/usr/bin/python3
"""This module defines a base class for future classes
 in this project."""


class Base:
    """Defines a base class."""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes the class."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
