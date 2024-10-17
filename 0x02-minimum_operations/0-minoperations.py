#!/usr/bin/python3
"""
module for minimum operations function
"""


def minOperations(n):
    """
    A function to calculate the minimum number of operations.
    """
    if n <= 1:
        return 0
    operations = 0
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1
    return operations
