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

    def update(self, *args, **kwargs):
        """Assigns value to attributes"""
        if args is not None and len(args) != 0:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        else:
            for Key, value in kwargs.items():
                if Key == "id":
                    self.id = value
                if Key == "size":
                    self.size = value
                if Key == "x":
                    self.x = value
                if Key == "y":
                    self.y = value

    def to_dictionary(self):
        """Return the dictionary representation of the square"""
        SqrDict = {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}
        return SqrDict
