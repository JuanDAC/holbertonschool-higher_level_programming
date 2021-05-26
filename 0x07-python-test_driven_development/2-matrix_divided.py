#!/usr/bin/python3
'''The module define with matrix_divided function'''


def matrix_divided(matrix, div):
    """A function to divide a matrix by a constant"""
    message = "matrix must be a matrix (list of lists) of integers/floats"
    if type(matrix) is not list or len(matrix) is 0:
        raise TypeError(message)
    for i in range(len(matrix)):
        if type(matrix[i]) != list:
            raise TypeError(message)
        if len(matrix[0]) != len(matrix[i]):
            raise TypeError(message)
        for cell in matrix[i]:
            if type(cell) not in [int, float]:
                raise TypeError(message)
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")
    div_lambda = lambda number: round((number / div), 2)
    return list(map(lambda row: list(map(div_lambda, row)), matrix))
