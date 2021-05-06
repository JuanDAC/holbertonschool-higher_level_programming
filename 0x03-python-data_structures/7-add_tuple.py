#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    len_max = 2
    array_a = [0 for i in range(len_max)]
    array_b = [0 for i in range(len_max)]
    for i in range(len_max):
        if (i < len(tuple_a)):
            array_a[i] = tuple_a[i];
        if (i < len(tuple_b)):
            array_b[i] = tuple_b[i];

    return (array_a[0] + array_b[0], array_a[1] + array_b[1])
