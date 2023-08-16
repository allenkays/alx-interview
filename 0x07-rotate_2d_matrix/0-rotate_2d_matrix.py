#!/usr/bin/python3
"""
Function to rotate a 2D matrix 90 degree in place
"""


def rotate_2d_matrix(matrix):
    """
    Function to rotate a 2D matrix

    Args:
        Matrix (List): List of lists
    """
    n = len(matrix)
    for i in range(n):
        for j in range(i, n):
            matrix[i][j],  matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in range(n):
        matrix[i].reverse()
