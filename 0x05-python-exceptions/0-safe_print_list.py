#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    number_characters = 0
    string = ""
    for i in range(x):
        try:
            string += "{}".format(my_list[i])
        except IndexError:
            break
        else:
            number_characters += 1
    print(string)
    return number_characters
