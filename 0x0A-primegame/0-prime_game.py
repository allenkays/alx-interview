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
    """
    Function to determine the winner in a game of picking prime numbers and
    their factors

    Args:
        x (int): input interger representing the number of rounds to be played
        nums (list): list of integers to selected from

    Returns:
        name (string): name of winner after all rounds are played
    """
    def play_round(current_player, remaining_numbers, memo):
        if not any(is_prime(num) for num in remaining_numbers):
            return "Ben" if current_player == "Maria" else "Maria"

        if (current_player, tuple(remaining_numbers)) in memo:
            return memo[(current_player, tuple(remaining_numbers))]

        winner = None
        for prime in primes:
            if prime in remaining_numbers:
                new_numbers = [
                        num for num in remaining_numbers if num % prime != 0
                ]
                other_player = "Maria" if current_player == "Ben" else "Ben"
                result = play_round(other_player, new_numbers, memo)
                if result == current_player:
                    winner = current_player
                    break

        memo[(current_player, tuple(remaining_numbers))] = winner
        return winner

    most_wins = {"Maria": 0, "Ben": 0}
    primes = calculate_primes(max(nums))

    for n in nums:
        winner = play_round("Maria", list(range(1, n + 1)), {})
        most_wins[winner] += 1

    if most_wins["Maria"] == most_wins["Ben"]:
        return None
    return "Maria" if most_wins["Maria"] > most_wins["Ben"] else "Ben"
