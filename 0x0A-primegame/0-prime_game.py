#!/usr/bin/python3
"""
Module for prime game
"""


def isWinner(x, nums):
    """
    returns the name of player that won the most rounds.
    """
    if x <= 0 or not nums:
        return None

    def sieve(n):
        """
        returns the list of primes.
        """
        is_prime = [True] * (n + 1)
        p = 2
        while p * p <= n:
            if is_prime[p]:
                for i in range(p * p, n + 1, p):
                    is_prime[i] = False
            p += 1
        prime_list = [p for p in range(2, n + 1) if is_prime[p]]
        return prime_list

    max_num = max(nums)
    primes = sieve(max_num)
    results = {0: "Ben"}

    for n in nums:
        count = 0
        for prime in primes:
            if prime > n:
                break
            count += 1
        
        if count % 2 == 0:
            results[n] = "Ben"
        else:
            results[n] = "Maria"

    maria_wins = sum(1 for key in nums if results[key] == "Maria")
    ben_wins = sum(1 for key in nums if results[key] == "Ben")

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
