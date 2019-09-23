"""
Selection problem:
    Input: A set A of n (distinct) numbers and an integer i , with 1 <= i <= n.
    Output: The element x in A that is larger than exactly i - 1 other elements of A.
"""
from IntroductionToAlgorithm3E.Chapter7.partition import random_partition, partition


def select_brute_force(array, i):
    # O(n * i) where i is in term of n <-> O(n^2)
    if len(array) == 1:
        return array[0]

    asc_list = []

    for loop in range(i + 1):
        current_min = array[0] if len(asc_list) == 0 else asc_list[len(asc_list) - 1]
        reset_current_min = False

        for x in array:
            if x in asc_list:
                continue
            elif len(asc_list) > 0 and x > current_min:
                if not reset_current_min:
                    current_min = x
                    reset_current_min = True
            elif x < current_min:
                current_min = x
            else:
                continue

        asc_list += [current_min]

    return asc_list[len(asc_list) - 1]


def select_using_sort(array, i):
    # utilize merge sort -> O(nlogn)
    if len(array) == 1:
        return array[0]

    array.sort()
    return array[i]


def select_partition(array, i, left=None, right=None):
    result = select_partition_capture_pivot(array, i, left, right)
    return result[1]


def select_partition_capture_pivot(array, i, left=None, right=None):
    # O(n)
    if len(array) == 1:
        return 0, array[0]

    left_index = 0 if left is None else left
    right_index = len(array) - 1 if right is None else right
    result = None
    pivot_index = None
    i += 1

    while left_index <= right_index:
        pivot_index = random_partition(array, left_index, right_index)
        k = pivot_index - left_index + 1

        if i == k:
            result = array[pivot_index]
            break
        elif i < k:
            right_index = pivot_index - 1
        else:
            left_index = pivot_index + 1
            i = i - k

    return pivot_index, result
