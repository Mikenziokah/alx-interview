#!/usr/bin/python3

""" function that determine the fewest number of coins
    needed to meet a given amount
"""


def makeChange(coins, total):
    """
    returns fewest number of coins needed to meet total
    """
    if not coins or coins is None:
        return -1
    if total <= 0:
        return -1
    change = 0
    coins = sorted(coins)[::-1]
    for coin in coins:
        while coin <= total:
            total -= coin
            change += 1
        if (total == 0):
            return change
    return 0
