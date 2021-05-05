#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    height = len(matrix)
    init = 0

    for i in range(init, height):
        width = len(matrix[i]);
        if not width:
            print("")
        for j in range(init, width):
            print(
                "{:d}".format(matrix[i][j]),
                end=('\n' if width == j + 1 else ' ')
            )
