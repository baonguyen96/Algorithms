"""
https://www.hackerrank.com/challenges/recursive-digit-sum/problem

Given an integer, we need to find the super digit of the integer.
    - If x has only 1 digit, then its super digit is x.
    - Otherwise, the super digit of x is equal to the super digit of the sum of the digits of x.

Given n and k, calculate super digit of new number p = n repeated k times
"""


def get_super_digit(n, k):
    total = _sum_all_digit(str(n)) * k
    return _get_supper_digit(str(total))


def _get_supper_digit(num_str):
    total = _sum_all_digit(num_str)

    if total < 10:
        return total
    else:
        return _get_supper_digit(str(total))


def _sum_all_digit(num_str):
    total = 0

    for digit in num_str:
        total += int(digit)         

    return total
