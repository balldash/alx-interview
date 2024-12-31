#!/usr/bin/python3
"""
Module for making change
"""


def makeChange(coins, total):
    """
    A greedy approach to making change
    """
    if total <= 0:
        return 0

    # Create a list to store the minimum number of coins for each value up to total
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # Base case: no coins needed to make 0 total

    for coin in coins:
        for amount in range(coin, total + 1):
            if dp[amount - coin] != float('inf'):
                dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
