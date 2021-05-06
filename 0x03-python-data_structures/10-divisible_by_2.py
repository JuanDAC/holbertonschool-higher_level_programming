#!/usr/bin/python3


def divisible_by_2(my_list=[]):
    return list(map(lambda x: True if not x % 2 else False, my_list))
