#!/usr/bin/python3
""" Return only the sub-class """


def inherits_from(obj, a_class):
    """
    Returns True if the object is an instance of a class
    that inherited from the specified class, otherwise False.
    """
    if type(obj) != a_class:
        return issubclass(type(obj), a_class)
    else:
        return False
