"""
Problem 5.1-2

Describe an implementation of the procedure
    RANDOM(a,b) that only makes calls to RANDOM(0,1).
    What is the expected running time of your procedure,
    as a function of aa and bb?
"""

import random


def get_random_number_brute_force(a, b):
    # O(b - a) - this is not really true because it assume
    # each time random.randint(0, 1) always return 1
    # this actually always returns a
    rand = random.randint(0, 1)

    while rand < a or rand > b:
        rand += random.randint(0, 1)

    return rand


def get_random_number_advance(a, b):
    # O(log(b - a))
    if a == b:
        return a

    while a < b:
        rand = random.randint(0, 1)
        mid = (a + b) // 2

        if rand == 0:
            b = mid
        else:
            a = mid

    return a
