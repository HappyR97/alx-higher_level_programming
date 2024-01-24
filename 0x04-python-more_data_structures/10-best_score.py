#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary is None or not a_dictionary:
        return None
    biggest_value = 0
    for key in a_dictionary:
        if a_dictionary[key] > biggest_value:
            biggest_value = a_dictionary[key]
            biggest_key = key
    return biggest_key
