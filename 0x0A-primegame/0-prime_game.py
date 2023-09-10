#!/usr/bin/python3
"""
Module: prime_game

This module defines a function for playing the prime game.
"""


def sieve_eratosthenes(limit):
    """
    Calculate prime numbers using the Sieve of Eratosthenes algorithm.

    Args:
        limit (int): The upper bound for generating prime numbers.

    Returns:
        list: A list of prime numbers less than or equal to the given limit.
    """
    sieve = [True] * (limit + 1)
    sieve[0:2] = [False, False]

    for current in range(2, int(limit**0.5) + 1):
        if sieve[current]:
            for multiple in range(current*current, limit + 1, current):
                sieve[multiple] = False

    primes = [num for num, is_prime in enumerate(sieve) if is_prime]
    return primes


def isWinner(x, nums):
    """
    Determine the winner of the prime game for multiple rounds.

    Args:
        x (int): The number of rounds.
        nums (list): A list of integers that are upper bounds for each round.

    Returns:
        str: The name of the player (Maria or Ben) who won the most rounds.
             If the winner cannot be determined, it returns "Ben" by default.
    """
    primes = sieve_eratosthenes(10000)

    def play_round(n):
        if n <= 1:
            return "Ben"  # Maria can't make a move, so Ben wins.

        count = sum(1 for prime in primes if prime <= n)
        if count % 2 == 0:
            return "Ben"
        else:
            return "Maria"

    winner_count = {"Maria": 0, "Ben": 0}

    for n in nums:
        winner = play_round(n)
        winner_count[winner] += 1

    if winner_count["Maria"] > winner_count["Ben"]:
        return "Maria"
    elif winner_count["Maria"] < winner_count["Ben"]:
        return "Ben"
    else:
        return "Ben"  # In case of a tie, we assume Ben wins.


# Example usage:
if __name__ == "__main__":
    x = 3
    nums = [4, 5, 1]
    print("Winner: {}".format(isWinner(x, nums)))
