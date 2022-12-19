#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        res = fct(*args)
        return res
    except Exception as err:
        sys.stdout.write("Exceptioon: " + str(err) + "\n")
        return
