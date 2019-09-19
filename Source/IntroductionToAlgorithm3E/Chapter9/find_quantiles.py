"""
Problem 9.3-6

The kth quantiles of an n-element set are the k - 1 order statistics
    that divide the sorted set into k equal-sized sets (to within 1).
    Give an O.n lg k/-time algorithm to list the kth quantiles of array set.
"""
from math import floor, ceil

from IntroductionToAlgorithm3E.Chapter7.partition import random_partition
from IntroductionToAlgorithm3E.Chapter9.selection import select_random_partition


def find_k_quantile(array, k, quantiles):
    if k == 1:
        return array
    else:
        n = len(array)
        i = floor(k / 2)
        partitions = i * floor(n / k)
        x = select_random_partition(array, partitions)
        x = random_partition(array, x)
        left = array[0:partitions]
        right = array[partitions + 1:n]
        quantiles += find_k_quantile(left, floor(k / 2), quantiles)
        quantiles += find_k_quantile(right, ceil(k / 2), quantiles)
        return x
