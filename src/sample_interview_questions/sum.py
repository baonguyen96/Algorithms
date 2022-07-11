"""
Write a program that, given int n, sums all whole number in [1..n] inclusive,
except for those that are divisible by 5 and 7
"""


def find_sum(n):
    total = 0

    for i in range(1, n + 1):
        if i % 5 == 0 or i % 7 == 0:
            continue

        total += i

    return total
