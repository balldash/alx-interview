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

    dp = [float('inf')] * (total + 1)
    dp[0] = 0
    for coin in coins:
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)
    return dp[total] if dp[total] != float('inf') else -1
