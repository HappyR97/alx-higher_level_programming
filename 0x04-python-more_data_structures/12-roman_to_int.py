#!/usr/bin/python3

def roman_to_int(roman_string):
    if type(roman_string) is not str or roman_string is None:
        return 0
    roman_values = {"I": 1, "V": 5, "X": 10, "L": 50,
                    "C": 100, "D": 500, "M": 1000}
    total = 0
    for i in range(len(roman_string)):
        if roman_string[i] == "V" and roman_string[i - 1] == 'I':
            total += 3
            continue
        if roman_string[i] == "X" and roman_string[i - 1] == 'I':
            total += 8
            continue
        if roman_string[i] == "L" and roman_string[i - 1] == "X":
            total += 30
            continue
        if roman_string[i] == "C" and roman_string[i - 1] == "X":
            total += 80
            continue
        if roman_string[i] == "D" and roman_string[i - 1] == "C":
            total += 300
            continue
        if roman_string[i] == "M" and roman_string[i  - 1] == "C":
            total += 800
            continue
        total += roman_values[roman_string[i]]
    return total
