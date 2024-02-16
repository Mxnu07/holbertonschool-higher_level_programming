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

        """Getters for width"""
        def get_width(self):
            """Returns the width of the rectangle."""
            return self.__width

        """Setters for width"""
        def set_width(self, width):
            """Sets the width of the rectangle."""
            self.__width = width

        """Getters for height"""
        def get_height(self):
            """Returns the height of the rectangle."""
            return self.__height

        """Setters for height"""
        def set_height(self, height):
            """Sets the height of the rectangle."""
            self.__height = height

        """Getters for x"""
        def get_x(self):
            """Returns the x of the rectangle."""
            return self.__x

        """Setters for x"""
        def set_x(self, x):
            """Sets the x of the rectangle."""
            self.__x = x

        """Getter for y"""
        def get_y(self):
            """Returns the y of the rectangle"""
            return self.__y

        """Setter for y"""
        def set_y(self, y):
            """Sets the y of the rectangle"""
            self.__y = y
