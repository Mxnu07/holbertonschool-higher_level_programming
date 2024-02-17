#!/usr/bin/python3
"""This module defines a class Rectangle that inherits from Base."""

from models.base import Base


class Rectangle(Base):
    """Defines a class Rectangle that inherits from Base."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes the class

        args:
            width (int)
            height (int)
            x (int)
            y (int)
            id (int)
        raises:
            TypeError: if either width or height is not an int
            ValueError: if either width or height is <= 0
            TypeError: if either of x or y is not an int
            ValueError: if either of x or y < 0
        """
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

    def update(self, *args, **kwargs):
        """Assigns key/value arguments to each attribute"""
        if args is not None and len(args) is not 0:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
            if len(args) >= 3:
                self.height = args[2]
            if len(args) >= 4:
                self.x = args[3]
            if len(args) >= 5:
                self.y = args[4]
        else:
            for Key, value in kwargs.items():
                if Key == "id":
                    self.id = value
                if Key == "width":
                    self.width = value
                if Key == "height":
                    self.height = value
                if Key == "x":
                    self.x = value
                if Key == "y":
                    self.y = value

    def to_dictionary(self):
        """Return the dictionary representation of the rectangle"""
        SqrDict = {'id': self.id, 'width': self.width, 'height': self.height,
                   'x': self.x, 'y': self.y}
        return (SqrDict)
