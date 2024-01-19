#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        i = 0
        for number in row:
            print("{:d}".format(number), end="")
            i += 1
            if i != len(row):
                print(" ", end="")
        print()
