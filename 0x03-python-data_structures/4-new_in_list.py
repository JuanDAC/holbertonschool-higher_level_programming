#!/usr/bin/python3


def new_in_list(my_list, idx, element):
    if not my_list:
        return

    new_array = []
    length = len(my_list)
    init = 0

    for i in range(init, length):
        new_array.append(my_list[i] if idx != i else element)
    return new_array
