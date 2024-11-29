#!/usr/bin/python3
"""
Module for making change
"""


def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet the given total

    Args:
    coins (list): List of coin denominations.
    total (int): Target amount.

    Returns:
    int: Minimum number of coins neede, or -1 if the total cannont be met.
    """
    if total <= 0:
        return 0

    coins.sort(reverse=True)
    count = 0

    for coin in coins:
        if total == 0:
            break
        count += total // coin
        total %= coin
    return count if total == 0 else -1
