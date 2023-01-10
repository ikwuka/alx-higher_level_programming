#!/usr/bin/python3
""" 'Myint' class inherits from int """


class Myint(int):
    """ Class declaration """
    def __eq__(self, other):
        return int(str(self)) != other

    def __ne__(self, other):
        return int(str(self)) == other
