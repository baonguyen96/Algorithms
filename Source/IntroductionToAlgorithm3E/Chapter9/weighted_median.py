"""
Find median and weighted median in O(n) time
For median, assume lower median if size is even
For weighted median, assume that weight is positive
"""


import math
import operator

from IntroductionToAlgorithm3E.Chapter9.selection import select_partition


def get_median_using_sort(array):
    # O(nlogn)
    array.sort()

    if len(array) % 2 == 0:
        mid_low = len(array) // 2 - 1
        median = array[mid_low]
    else:
        mid = math.floor(len(array) / 2)
        median = array[mid]

    return median


def get_median_using_select(array):
    # O(n)
    if len(array) % 2 == 0:
        mid_index = len(array) // 2 - 1
    else:
        mid_index = len(array) // 2
    return select_partition(array, mid_index)


def get_weighted_median_using_sort(array):
    # O(nlogn)
    array = sorted(array, key=operator.itemgetter(0))
    current_weight_sum = 0
    value = 0
    weight = 1
    weighted_median = None
    total_weight = 0

    for pair in array:
        total_weight += pair[weight]

    for pair in array:
        if current_weight_sum + pair[weight] >= total_weight / 2 > current_weight_sum:
            weighted_median = pair[value]
            break

        current_weight_sum += pair[weight]

    return weighted_median


def get_weighted_median_using_select(array):
    # O(n) time, but not space-efficient

    # find largest decimal places of the weight
    largest_decimal_place = 0

    for pair in array:
        current_decimal_places = str(pair[1])[::-1].find('.')

        if current_decimal_places == -1:
            current_decimal_places = 0
        elif int(str(pair[1])[-current_decimal_places:]) == 0:
            current_decimal_places = 0

        if current_decimal_places > largest_decimal_place:
            largest_decimal_place = current_decimal_places

    mult_factor = 10 ** largest_decimal_place

    # construct 1d array of values by O(n)
    values = []
    for pair in array:
        rep = pair[1] * mult_factor
        values += [pair[0]] * int(rep)

    # normal select in O(n)
    weighted_median = get_median_using_select(values)

    return weighted_median

