"""
Find all subsets in a set with distinct elements (powerset)
O(2^n) time
"""


def get_all_subsets(array):
    subsets = []

    for i in array:
        subsets += [[i]]
        for subset in subsets:
            if i not in subset:
                new_subset = subset + [i]
                subsets += [new_subset]

    subsets = [[]] + subsets
    return subsets
