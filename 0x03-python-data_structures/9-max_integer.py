#!/usr/bim/python3


def max_integer(my_list=[]):
    currentItem = my_list[0] if len(my_list) else None
    for i in range(len(my_list)):
        if currentItem < my_list[i]:
            currentItem = my_list[i]
    return currentItem
