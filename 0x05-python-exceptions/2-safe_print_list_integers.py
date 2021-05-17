#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0):
    string = ""
    for i in range(x):
        try:
            string += "{:d}".format(my_list[i])
        except IndexError:
            i -= 2
            break
        except ValueError:
            i -= 1
            continue
        except TypeError:
            i -= 1
            continue
    print(string)
    return i
