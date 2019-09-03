"""
Problem 2.3-7

Describe a O(nlogn)-time algorithm that,
    given a set S of n integers and another integer x,
    determines whether or not there exist two elements in S
    whose sum is exactly x.
"""

from Source.Utitilies.utility import binary_search


def exist_elements_with_sum_brute_force(s, x):
    # O(n^2)
    found = False

    for a in s:
        for b in s:
            if a + b == x:
                found = True
                break

    return found


def exist_elements_with_sum_enhance(s, x):
    # O(nlogn)
    s.sort()
    found = False

    for i in s:
        j = x - i

        if binary_search(s, j) > -1:
            found = True
            break

    return found
