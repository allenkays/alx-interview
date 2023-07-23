#!/usr/bin/python3
"""
This script calculate the minimum number of operations need to
get n H characters copied over.
"""


def minOperations(n):
    """
    Calculates the fewest number of operations needed to result
    in exactly n H characters in the file.

    Args:
        n (int): Number of of characters needed

    Returns:
         int: minimum number of ops needed to get n H characters in a file
    """
    if n == 1:
        return 0

    ops = 0
    factor = 2

    while n > 1:
        if n % factor == 0:
            n //= factor
            ops += factor
        else:
            factor += 1

    return ops
