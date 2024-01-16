#!/usr/bin/python3
def remove_char_at(str, n):
    str1 = str[:n]
    str2 = str[n+1:]
    if n < 0:
        return str
    else:
        return str1 + str2
