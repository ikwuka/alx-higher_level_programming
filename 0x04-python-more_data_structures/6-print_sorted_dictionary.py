#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    ordered = sorted(a_dictionary)
    for i in ordered:
        print("{}: {}".format(i, a_dictionary[i]))
