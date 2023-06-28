#!/usr/bin/python3
"""
0-pascal_triangle.py
"""


def pascal_triangle(n):
    """
    Takes in an interger n and returns the pascals triangle

    Args:
        n: int

    Returns:
        iterable list: forming pascals triangle.
    """
    if n <= 0:
        return []

    triangle = [[1]]
    """"
    for i in range(0,n):
        row = [1]
        if i > 0:
            prev_row = triangle[i-1]
            for j in range(len(prev_row)-1):
                row.append(prev_row[j] + prev_row[j+1])
            row.append(1)
        triangle.append(row)
    """
    for i in range(1, n):
        row = [1] + [
                triangle[i - 1][j] + triangle[i - 1][j + 1]
                for j in range(i-1)] + [1]
        triangle.append(row)

    return triangle
