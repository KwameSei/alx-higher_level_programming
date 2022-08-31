#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    list_2 = []
    for x in matrix:
        list_2.append(list(map(lambda x: x ** 2, x)))
    return (list_2)
