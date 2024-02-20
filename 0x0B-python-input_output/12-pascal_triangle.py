#!/usr/bin/python3

"""

This module defines a function that returns a list of lists
of integers representing the Pascal's triangle

"""


def pascal_triangle(n):
    """Returns Pascal's triange (list of lists)"""
    my_list = []
    if n <= 0:
        return my_list

    for i in range(n):
        row = []
        for j in range(i + 1):
            row.append(comb(i, j))
        my_list.append(row)

    return my_list


def factorial(n):
    """Calculate the factorial of n."""
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)


def comb(n, k):
    """Calculate the number of combinations of n items taken k at a time."""
    return factorial(n) // (factorial(k) * factorial(n - k))
