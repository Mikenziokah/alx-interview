#!/usr/bin/python3
""" minoperations module
"""


def minOperations(n):
    """a method that calculates the fewest number of operations
        needed to result in exactly n H characters in a file.
    """
    # outputs should be 2 characters
    if (n < 2):
        return 0
    x, root = 0, 2
    while root <= n:
        # if n evenly devides by root
        if n % 2 == 0:
            # total evens divisible by root = total operations(x)
            x += root
            # give n to the reminder
            n = n / root
            # decrement root to find remaining smaller vals to evenly devide n
            root -= 1
            # increment root untill it evenly devides by n
            root += 1
            # return operations(x)
            return x
