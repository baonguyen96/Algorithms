"""
Problem 9.3-6

The kth quantiles of an n-element set are the k - 1 order statistics
    that divide the sorted set into k equal-sized sets (to within 1).
    Give an O(nlgk) time algorithm to list the kth quantiles of array set.
"""

from IntroductionToAlgorithm3E.Chapter7.partition import partition
from IntroductionToAlgorithm3E.Chapter9.selection import select_partition, select_partition_capture_pivot


def find_k_quantiles(array, k):
    if k == 1:
        return array
    else:
        mid_index = len(array) // 2
        median, pivot_index = select_partition_capture_pivot(array, mid_index)
        partition(array, pivot_index)

        left = find_k_quantiles(array[:mid_index], k // 2)
        right = find_k_quantiles(array[mid_index + 1:], k // 2)
        return left + [median] + right
