#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    string = ""
    for i in range(x):
        try:
            string += "{}".format(my_list[i])
        except IndexError:
            i -= 1
            break
    print(string)
    try:
        i += 1
    except UnboundLocalError:
        i = 0
    return i
