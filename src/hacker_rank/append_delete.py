"""
https://www.hackerrank.com/challenges/append-and-delete/problem

You have a string of lowercase English alphabetic letters. You can perform two types of operations on the string:
    - Append a lowercase English alphabetic letter to the end of the string.
    - Delete the last character in the string. Performing this operation on an empty string results in an empty string.
Given an integer k, and two strings s and t, determine whether or not you can convert s to t by performing exactly
    k of the above operations on s. If it's possible, print Yes. Otherwise, print No.
"""


def is_transformation_possible(source, destination, steps):
    i = 0

    for i in range(min(len(source), len(destination))):
        if source[i] != destination[i]:
            break

    backfill = len(source) - i
    backfill += len(destination) - i

    return backfill <= steps
