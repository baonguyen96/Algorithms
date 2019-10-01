"""
Problem 9.3-7

Describe an O(n) time algorithm that,
    given a set S of n distinct numbers and a positive integer k <= n,
    determines the k numbers in S that are closest to the median of S.
    Note that the order of each elements within the result
    does not matter, as long as those elements are the closest to k.
"""
from IntroductionToAlgorithm3E.Chapter9.selection import select_partition_capture_pivot
import Utitilies.utility as util


def find_k_elements_closest_to_median(array, k):
    if array is None or len(array) == 0 or k == 0:
        return []

    k_org = k
    if not util.is_even(k):
        k += 1

    # lower median
    median_index, median_value = select_partition_capture_pivot(array, len(array) // 2)

    left_array = array[:median_index]
    left_most_index, left_most_value = \
        select_partition_capture_pivot(left_array, median_index - k // 2)

    right_array = array[median_index:]
    right_most_index, right_most_value = \
        select_partition_capture_pivot(right_array, k // 2)

    # right_most_index += median_index
    # array = left_array + right_array

    if not util.is_even(k_org):
        right_most_index -= 1
        right_most_value = right_array[right_most_index]

    return left_array[left_most_index:median_index] + right_array[1:right_most_index + 1]
