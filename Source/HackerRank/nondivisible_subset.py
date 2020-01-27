"""
Given a set of distinct integers, print the size of a maximal subset of S
    where the sum of any 2 numbers in S' is not evenly divisible by k.
"""


def count_subset_not_divisible_by_k(arr, k):
    size = len(arr)

    for i in range(len(arr) - 1):
        i_pair_divisible = 0

        for j in range(i + 1, len(arr)):
            if (arr[i] + arr[j]) % k == 0:
                i_pair_divisible += 1

        if i_pair_divisible == (len(arr) - i):
            size -= 1

    return size
