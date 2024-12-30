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
    check = 0
    temp = 0
    coins.sort(reverse=True)
    for i in coins:
        while check < total:
            check += 1
            temp += 1
        if check == total:
            return temp
        check -= 1
        temp -= 1
    return -1
