#!/usr/bin/python3
""" This module that contains a function which reads from a file """


def read_file(filename=""):
    """
    Function that reads from a file

    Args:
        filename: filename

    Raises:
        Exception: when the file can be opened
    """

    with open(filename, "r", encoding="utf-8") as f:
        read_data = f.read()
        print(read_data, end="")
