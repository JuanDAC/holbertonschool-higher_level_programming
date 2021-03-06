#!/usr/bin/python3

"""A class used to represent an Animal"""


class Rectangle:
    """A class used to represent an Animal"""

    def __init__(self, width=0, height=0):
        """__init__ class used to represent an Animal"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """width class used to represent an Animal"""
        return self.__width

    @width.setter
    def width(self, value):
        """width class used to represent an Animal"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise TypeError("width must be >= 0")
        else:
            self.__width = value

    @property
    def heigth(self):
        """height class used to represent an Animal"""
        return self.__heigth

    @heigth.setter
    def height(self, value):
        """height class used to represent an Animal"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise TypeError("height must be >= 0")
        else:
            self.__height = value


if __name__ == "__main__":
    try:
        my_rectangle = Rectangle(2, -3)
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    try:
        my_rectangle = Rectangle(-2, 3)
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))
