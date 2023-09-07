#!/usr/bin/python3
"""
0. Prime Game
"""


def is_prime(n):
    """
    Function to check if number is prime or not

    Args:
        n (int): interger to check

    Returns:
        boolean : True or False
    """
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def calculate_primes(n):
    primes = []
    for i in range(2, n + 1):
        if is_prime(i):
            primes.append(i)
    return primes


def isWinner(x, nums):
    def play_round(n):
        if n <= 1:
            return "Maria"

        primes = calculate_primes(n)
        if len(primes) % 2 == 0:
            return "Maria"
        else:
            return "Ben"

    winner_count = {"Maria": 0, "Ben": 0}

    for n in nums:
        winner = play_round(n)
        winner_count[winner] += 1

    if winner_count["Maria"] > winner_count["Ben"]:
        return "Maria"
    elif winner_count["Maria"] < winner_count["Ben"]:
        return "Ben"
    else:
        return "Ben"
