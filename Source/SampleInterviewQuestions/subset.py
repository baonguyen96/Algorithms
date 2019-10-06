"""
(1)
Find all subsets in a set with distinct elements (powerset) O(2^n) time

(2)
Then find all subsets who sum is a given number.
Assume all positive number and no duplicated.
"""
from Utitilies.utility import get_all_binaries_for_length


def get_all_subsets(array):
    subsets = []
    combinations = get_all_binaries_for_length(len(array))

    for r in range(len(combinations)):
        subset = []

        for c in range(len(combinations[r])):
            if combinations[r][c]:
                subset += [array[c]]

        subsets += [subset]

    return subsets


def count_subsets_with_sum(arrays, s):
    subsets = get_all_subsets(arrays)
    count = 0

    for subset in subsets:
        if sum(subset) == s:
            count += 1

    return count
