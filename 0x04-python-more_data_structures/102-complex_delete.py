#!/usr/bin/python3


def complex_delete(a_dictionary, value):
    key = 0
    val = 1

    if a_dictionary is None:
        return None

    for item in a_dictionary.items():
        if value == item[val]:
            del item[key]

    return a_dictionary
