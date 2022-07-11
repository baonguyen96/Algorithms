"""
Problem 16-1 Coin changing

Consider the problem of making change for n cents using the fewest number of coins.
    Assume that each coin’s value is an integer
"""
from math import ceil


def make_coin_change(amount):
    amount = int(amount * 100)

    quarter_count = amount // 25
    amount = amount % 25

    dime_count = amount // 10
    amount = amount % 10

    nickle_count = amount // 5

    penny_count = amount % 5

    return [quarter_count, dime_count, nickle_count, penny_count]


def make_coin_change_loop(amount):
    quarter_count = 0
    dime_count = 0
    nickle_count = 0
    penny_count = 0

    for i in range(ceil(amount / 0.25)):
        new_amount = amount - 0.25

        if new_amount < 0:
            break

        quarter_count += 1
        amount = round(new_amount, 2)

    for i in range(ceil(amount / 0.1)):
        new_amount = amount - 0.1

        if new_amount < 0:
            break

        dime_count += 1
        amount = round(new_amount, 2)

    for i in range(ceil(amount / 0.05)):
        new_amount = amount - 0.05

        if new_amount < 0:
            break

        nickle_count += 1
        amount = round(new_amount, 2)

    penny_count = ceil(amount * 100)

    return [quarter_count, dime_count, nickle_count, penny_count]
