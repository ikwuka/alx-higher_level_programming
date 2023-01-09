#!/usr/bin/python3
"""
Returns True (if the object is exactly an
instance of the specified class), else False.
"""


def is_same_class(obj, a_class):
    """ Returns True if the object is an instance """
    return True if type(obj) == a_class else False
