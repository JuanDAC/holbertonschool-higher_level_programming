#!/usr/bin/python3

"""Class docstrings go here."""


class Square:
    """Class docstrings go here."""

    def __init__(self, size=0):
        """__init__ constructor method."""
        self.size = size

    def area(self):
        """area that returns the current square area."""
        return self.__size ** 2

    @property
    def size(self):
        """size to retrieve it."""
        return self.__size

    @size.setter
    def size(self, value):
        """setter to set it."""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value


if __name__ == "__main__":
    my_square = Square(89)
    print("Area: {} for size: {}".format(my_square.area(), my_square.size))

    my_square.size = 3
    print("Area: {} for size: {}".format(my_square.area(), my_square.size))

    try:
        my_square.size = "5 feet"
        print("Area: {} for size: {}".format(my_square.area(), my_square.size))
    except Exception as e:
        print(e)
