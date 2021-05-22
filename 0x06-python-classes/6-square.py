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
        size = self.size
        not self.size and print()
        size and print(self.position[1] * "\n", end="")
        [print(self.position[0] * " " + size * "#") for _ in range(size)]


if __name__ == "__main__":
    my_square_1 = Square(3)
    my_square_1.my_print()

    print("--")

    my_square_2 = Square(3, (1, 1))
    my_square_2.my_print()

    print("--")

    my_square_3 = Square(3, (3, 0))
    my_square_3.my_print()

    print("--")
