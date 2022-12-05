#!/usr/bin/python3
def no_c(my_string):
    rev = ""
    for index in range(0, len(my_string)):
        if my_string[index] != 'c' and my_string[index] != 'C':
            rev = rev + my_string[index]
    return rev
