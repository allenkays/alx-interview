#!/usr/bin/python3
"""
Function to calculate the fewest number of coins to meet given total;
"""


def makeChange(coins, total):
    """
    Function to return change

    Args:
        coins (list): list containing coins of different values
        total (int): total needed for number of coins

    Returns:
        coin_count (int): difference between sum total of coins and sum
    """
    coins.sort(reverse=True)
    coin_count = 0

    for coin in coins:
        while total >= coin:
            total -= coin
            coin_count += 1
    return coin_count if total == 0 else -1
