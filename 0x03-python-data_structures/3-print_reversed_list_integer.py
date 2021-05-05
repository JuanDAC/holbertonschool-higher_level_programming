#!/usr/bin/python3


def print_reversed_list_integer(my_list=[]):
    length = len(my_list)

    for i in range(1, length + 1):
        print("{:d}".format(my_list[i * -1]))
