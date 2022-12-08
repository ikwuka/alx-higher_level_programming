#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dict = dict(a_dictionary)
    for i in a_dictionary:
        new_dict[i] *= 2
    return new_dict
