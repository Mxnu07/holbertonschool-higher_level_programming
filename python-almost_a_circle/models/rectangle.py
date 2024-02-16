#!/usr/bin/python3
"""This module defines a class Rectangle that inherits from Base."""

from models.base import Base


class Rectangle(Base):
    """Defines a class Rectangle that inherits from Base."""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes the class."""

        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

        @property
        def width(self):
            """Returns the width of the rectangle."""
            return self.__width

        @width.setter
        def width(self, value):
            """Sets the width of the rectangle."""
            self.__width = value

        @property
        def get_height(self):
            """Returns the height of the rectangle."""
            return self.__height

        @height.setter
        def set_height(self, value):
            """Sets the height of the rectangle."""
            self.__height = value

        @property
        def get_x(self):
            """Returns the x of the rectangle."""
            return self.__x

        @x.setter
        def set_x(self, value):
            """Sets the x of the rectangle."""
            self.__x = value

        @property
        def get_y(self):
            """Returns the y of the rectangle"""
            return self.__y

        @y.setter
        def set_y(self, value):
            """Sets the y of the rectangle"""
            self.__y = value
