#!/usr/bin/python3

def weight_average(my_list=[]):
    if not my_list or my_list is None:
        return 0
    score = 0
    weight = 0
    for element in my_list:
        score += (element[0] * element[1])
        weight += element[1]
    return score / weight
