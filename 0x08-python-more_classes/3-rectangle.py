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
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise TypeError("width must be >= 0")
        self.__width = value

    @property
    def heigth(self):
        """width class used to represent an Animal"""
        return self.__height

    @heigth.setter
    def height(self, value):
        """height class used to represent an Animal"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise TypeError("height must be >= 0")
        self.__height = value

    def perimeter(self):
        return (self.heigth + self.width) * 2

    def area(self):
        return self.heigth * self.width

    def __string__(self):
        return [print(self.width * "#") for _ in self.heigth]

if __name__ == "__main__":
    my_rectangle = Rectangle(2, 4)
    print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))

    print(str(my_rectangle))
    print(repr(my_rectangle))

    print("--")

    my_rectangle.width = 10
    my_rectangle.height = 3
    print(my_rectangle)
    print(repr(my_rectangle))
