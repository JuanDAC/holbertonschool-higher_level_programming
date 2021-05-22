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
        if not self.size:
            print()
        print(self)

    def __str__(self):
        """__string__ that prints in stdout the square with the character #"""
        string = ""
        size = self.size
        if size:
            string += (self.position[1] * "\n")
        for i in range(size):
            newline = "\n" if (size - 1 != i) else ""
            string += (self.position[0] * " " + size * "#") + newline
        return string

    def __eq__(self, other):
        """__eq__ that prints in stdout the square with the character #"""
        return (self.area() == other.area())

    def __ne__(self, other):
        """__ne__ that prints in stdout the square with the character #"""
        return (self.area() != other.area())

    def __lt__(self, other):
        """__lt__ that prints in stdout the square with the character #"""
        return (self.area() < other.area())

    def __le__(self, other):
        """__le__ that prints in stdout the square with the character #"""
        return (self.area() <= other.area())

    def __gt__(self, other):
        """__gt__ that prints in stdout the square with the character #"""
        return (self.area() > other.area())

    def __ge__(self, other):
        """__ge__ that prints in stdout the square with the character #"""
        return (self.area() >= other.area())


if __name__ == "__main__":
    s_5 = Square(5)
    s_6 = Square(6)

    if s_5 < s_6:
        print("Square 5 < Square 6")
    if s_5 <= s_6:
        print("Square 5 <= Square 6")
    if s_5 == s_6:
        print("Square 5 == Square 6")
    if s_5 != s_6:
        print("Square 5 != Square 6")
    if s_5 > s_6:
        print("Square 5 > Square 6")
    if s_5 >= s_6:
        print("Square 5 >= Square 6")
