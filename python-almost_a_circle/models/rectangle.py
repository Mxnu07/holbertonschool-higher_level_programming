#!/usr/bin/python3
"""This module defines a class Rectangle that inherits from Base."""

from models.base import Base


class Rectangle(Base):
    """Defines a class Rectangle that inherits from Base."""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes the class."""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

        @property
        def width(self):
            """Returns the width of the rectangle."""
            return self.__width

        @width.setter
        def width(self, value):
            """Sets the width of the rectangle."""
            if type(value) is not int:
                raise TypeError("width must be an integer")
            if value <= 0:
                raise ValueError("width must be > 0")
            self.__width = value

        @property
        def height(self):
            """Returns the height of the rectangle."""
            return self.__height

        @height.setter
        def height(self, value):
            """Sets the height of the rectangle."""
            if type(value) is not int:
                raise TypeError("height must be an integer")
            if value <= 0:
                raise ValueError("height must be > 0")
            self.__height = value

        @property
        def x(self):
            """Returns the x of the rectangle."""
            return self.__x

        @x.setter
        def x(self, value):
            """Sets the x of the rectangle."""
            if type(value) is not int:
                raise TypeError("x must be an integer")
            if value < 0:
                raise ValueError("x must be >= 0")
            self.__x = value

        @property
        def y(self):
            """Returns the y of the rectangle"""
            return self.__y

        @y.setter
        def y(self, value):
            """Sets the y of the rectangle"""
            if type(value) is not int:
                raise TypeError("y must be an integer")
            if value < 0:
                raise ValueError("y must be >= 0")
            self.__y = value

        def area(self):
            """Returns the area of rectangle"""
            return self.width * self.height

        def display(self):
            """Displays the rectangle"""
            rectangle = self.y * "\n"
            for i in range(self.height):
                rectangle += (" " * self.x)
                rectangle += ("#" * self.width) + "\n"

            print(rectangle, end='')

        def __str__(self):
            """Str special method"""
            return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                           self.x, self.y,
                                                           self.width,
                                                           self.height)
