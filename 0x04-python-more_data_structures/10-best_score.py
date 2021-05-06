#!/usr/bin/python3


def best_score(a_dictionary):
    value = 1
    key = 0
    my_list = a_dictionary.items() if a_dictionary else []
    currentItem = my_list[0] if len(my_list) else (None,)

    for i in range(len(my_list)):
        if currentItem[value] < my_list[i][value]:
            currentItem = my_list[i]
    return currentItem[key]
