"""
Problem 9.3-7

Describe an O(n) time algorithm that,
    given a set S of n distinct numbers and a positive integer k <= n,
    determines the k numbers in S that are closest to the median of S
"""
from IntroductionToAlgorithm3E.Chapter9.selection import select_partition_capture_pivot
import Utitilies.utility as util


def find_k_elements_closest_to_median(array, k):
    if array is None or len(array) == 0 or k == 0:
        return []

    k_org = k
    if not util.is_even(k):
        k += 1

    median_value, median_index = select_partition_capture_pivot(array, len(array) // 2)
    left_most_value, left_most_index = \
        select_partition_capture_pivot(array[:median_index], median_index - k // 2)
    right_most_value, right_most_index = \
        select_partition_capture_pivot(array[median_index + 1:], k // 2)

    if not util.is_even(k_org):
        if util.get_difference(median_value, array[left_most_index]) > \
                util.get_difference(median_value, array[right_most_index]):
            left_most_index += 1
            left_most_value = array[left_most_index]
        else:
            right_most_index -= 1
            right_most_value = array[right_most_index]

    return array[left_most_index:median_index] + array[median_index + 1:right_most_index]
