#!/usr/bin/python3


def roman_to_int(roman_string):
    """
               0,   1,   2,   3,   4,   5,    6
               1,   5,  10,   50, 100, 500, 1000
    """
    numbers = ["I", "V", "X", "L", "C", "D", "M"]
    number = 0
    roman_list = list(roman_string)
    roman_len = len(roman_list) - 1
    for i, character in enumerate(roman_list):
        index = numbers.index(character)
        scale = (index - 2) if (index % 2) else (index - 1)
        scale = 0 if (scale == -1) else scale
        base = 5 if (index % 2) else 1
        if i < roman_len and numbers.index(roman_list[i + 1]) > index:
            number -= ((10 ** scale) or 1) * base
        else:
            number += ((10 ** scale) or 1) * base
    return number
