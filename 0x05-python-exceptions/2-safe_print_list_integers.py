#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0):
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            (string)
        except ValueError:
            i -= 1
            continue
        except TypeError:
            i -= 1
            continue
    print("")
    return i
