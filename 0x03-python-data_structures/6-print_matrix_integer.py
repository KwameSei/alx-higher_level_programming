#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for a in matrix:
        for b in a:
            if a.index(b) < len(a) - 1:
                print("{:d}".format(b), end=" ")
            else:
                print("{:d}".format(b), end="")
        print()
