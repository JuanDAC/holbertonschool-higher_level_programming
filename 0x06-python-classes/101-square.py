#!/usr/bin/python3


"""File with class Square"""


class Square:
    """Class use to represent a Square"""
    def __init__(self, size=0, position=(0, 0)):
        """__init__ constructor method"""
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) is not tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        for i in range(len(value)):
            if type(value[i]) is not int or value[i] < 0:
                raise TypeError(
                        "position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """area that returns the current square area"""
        return self.size ** 2

    def my_print(self):
        """my_print that prints in stdout the square with the character #"""
        print(self)

    def __str__(self):
        """__string__ that prints in stdout the square with the character #"""
        string = ""
        size = self.size
        if not self.size:
            string += "\n"
        if size:
            string += (self.position[1] * "\n")
        for _ in range(size):
            string += (self.position[0] * " " + size * "#") + "\n"
        return string


if __name__ == "__main__":
    my_square = Square(5, (0, 0))
    print(my_square)

    print("--")

    my_square = Square(5, (4, 1))
    print(my_square)

    print("--")

    my_square.my_print()
