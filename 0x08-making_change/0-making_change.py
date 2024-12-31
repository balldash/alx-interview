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
    def dp(amount, memo):
        if amount in memo:
            return memo[amount]
        if amount == 0:
            return 0
        if amount < 0:
            return float('inf')

        min_coins = float('inf')
        for coin in coins:
            num_coins = dp(amount - coin, memo) + 1
            min_coins = min(min_coins, num_coins)

        memo[amount] = min_coins
        return memo[amount]
    if total <=0:
        return 0
    result = dp(total, {})
    return result if result != float('inf') else -1

