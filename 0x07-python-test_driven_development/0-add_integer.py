#!/usr/bin/python3
"""
This is the Add Integer module.

This module supplies one function (add_integer()),
- that adds two integer and float together - returning
an integer.
"""


def add_integer(a, b=98):
    """
    Return the sum of of two numbers - integer and float.
    Otherwise, raise a TypeError for given incorrect argument.
    """
    h = list(map(lambda x: isinstance(x, (int, float)), [a, b]))

    if all(h):
        return int(a) + int(b)

    for x, y in list(zip(h, ["a", "b"])):
        if not x:
            raise TypeError("{} must be an integer".format(y))
