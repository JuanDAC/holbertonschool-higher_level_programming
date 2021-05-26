#!/usr/bin/python3
""" add integer """


def add_integer(a, b=98):
    """ add integer """

    if type(a) not in [float, int]:
        raise TypeError("a must be an integer")

    if type(b) not in [float, int]:
        raise TypeError("b must be an integer")

    return int(a) + int(b)
