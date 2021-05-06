#!/usr/bin/python3


def delete_at(my_list=[], idx=0):
    old_list = my_list[:]
    length = len(my_list)
    del my_list[:]
    for i in range(length):
        if (i != idx):
            my_list.append(old_list[i])
    return my_list
