#!/usr/bin/python3


def multiply_by_2(a_dictionary):
    new_dictionary = None

    if a_dictionary is None:
        return new_dictionary

    new_dictionary = a_dictionary.copy()

    for key in new_dictionary.keys():
        new_dictionary[key] *= 2

    return new_dictionary
