#!/usr/bin/python3


def search_replace(my_list, search, replace):
    return list(
        map(lambda value: value if value != search else replace,
        my_list)
    )

