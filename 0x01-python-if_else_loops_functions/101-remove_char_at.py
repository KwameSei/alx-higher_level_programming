#!/usr/bin/python3

def remove_char_at(str, n):
    string = ""
    for x in range(0, len(str)):
        if x == n:
            continue
        string = string + str[x]
    return string
