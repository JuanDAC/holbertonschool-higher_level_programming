#!/usr/bin/python3


def no_c(my_string):

    new_string = ""
    length = len(my_string)
    init = 0

    for i in range(init, length):
        if my_string[i] != 'c' or my_string[i] != 'C':
            new_string += my_string[i]
    return new_string
