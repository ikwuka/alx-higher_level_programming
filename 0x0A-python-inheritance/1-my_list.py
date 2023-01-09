#!/usr/bin/python3
""" The MyList class inherits from list """


class MyList(list):
    """ Inherits from list """
    def print_sorted(self):
        """ prints the list, but sorted in an ascending order """
        print(sorted(self))
