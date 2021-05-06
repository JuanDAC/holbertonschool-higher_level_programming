#!/usr/bin/python3


def my_format(a_dictionary):
    def warp(key):
        print("{}: {}".format(key, a_dictionary[key]))
    return warp


def print_sorted_dictionary(a_dictionary):
    return map(my_format(a_dictionary), sorted(a_dictionary))
