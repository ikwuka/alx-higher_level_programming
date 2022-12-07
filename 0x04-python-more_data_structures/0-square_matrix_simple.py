#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for i in matrix:
        new_matrix[len(new_matrix):] = [[elem ** 2 for elem in i]]
    return new_matrix
