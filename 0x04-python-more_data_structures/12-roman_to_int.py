#!/usr/bin/python3

def roman_to_int(roman_string):
    roman_values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    total = 0
    for c in roman_string:
        total += roman_values[c]
    return total
