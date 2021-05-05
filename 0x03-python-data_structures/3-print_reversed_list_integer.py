#!/usr/bin/python3


def print_reversed_list_integer(my_list=[]):
    if not my_list:
        return
    length = len(my_list)
    init = 1

    for i in range(init, length + 1):
        print("{:d}".format(my_list[i * -1]))

