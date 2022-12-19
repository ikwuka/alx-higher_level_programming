#!/usr/bin/python3
def safe_print_division(a, b):
    total = 0
    try:
        total = a / b
        return total
    except ZeroDivisionError:
        total = None
        return total
    finally:
        print("Inside result: {}".format(total))
