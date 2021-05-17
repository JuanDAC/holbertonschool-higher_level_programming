#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    new_line = []
    for i in range(list_length):
        try:
            value = my_list_1[i] / my_list_2[i]
        except TypeError:
            value = 0
            print("wrong type")
        except ZeroDivisionError:
            value = 0
            print("division by 0")
        except IndexError:
            print("out of range")
            value = 0
        finally:
            new_line.append(value)
    return new_line
