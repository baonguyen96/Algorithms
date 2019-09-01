"""
Problem 2.3-7

Describe a O(nlogn)-time algorithm that,
    given a set S of n integers and another integer x,
    determines whether or not there exist two elements in S
    whose sum is exactly x.
"""

from Source.Utitilies.utility import binary_search, get_random_array


def exist_elements_with_sum(s, x):
    s.sort()
    found = False

    for i in s:
        j = x - i

        if binary_search(s, j) > -1:
            found = True
            break

    return found
