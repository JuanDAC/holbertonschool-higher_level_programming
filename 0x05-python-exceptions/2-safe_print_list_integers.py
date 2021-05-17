#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0):
    number_characters = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
        except (ValueError, TypeError):
            continue
        else:
            number_characters += 1
    print("")
    return number_characters
