#!/usr/bin/python3
"""This module defines a class Square that inherits from Base."""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Defines the class Square that inherits from Rectangle."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize the class"""
        self.size = size
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Return size attribute"""
        return self.width

    @size.setter
    def size(self, value):
        """Sets size attribute to value"""
        self.width = value
        self.height = value

    def __str__(self):
        """Str special method"""
        return "[Square] ({}) {}/{} - {}".format(self.id,
                                                 self.x, self.y,
                                                 self.width)
