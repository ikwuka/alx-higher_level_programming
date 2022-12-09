#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return lsit(*map(lambda a : list(map(lambda b : b*b, a)), matrix))
