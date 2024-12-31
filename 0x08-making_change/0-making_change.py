#!/usr/bin/python3
"""
Module for making change
"""


def makeChange(coins, total):
    """
    A function to calculate the change.
    """
    def dp(amount, memo):
        """
        A dynamic function to break down the problem better.
        """
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

    if total <= 0:
        return 0
    
    result = dp(total, {})
    return result if result != float('inf') else -1
