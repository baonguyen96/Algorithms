import math
import operator


def get_median(array):
    array.sort()

    if len(array) % 2 == 0:
        mid_low = len(array) // 2 - 1
        mid_high = len(array) // 2
        median = (array[mid_low] + array[mid_high]) / 2
    else:
        mid = math.floor(len(array) / 2)
        median = array[mid]

    return median


def get_weighted_median(array):
    array = sorted(array, key=operator.itemgetter(0))
    current_sum = 0
    value = 0
    weight = 1
    wm = 0
    total_weight = 0

    for pair in array:
        total_weight += pair[weight]

    for pair in array:
        if current_sum + pair[weight] >= total_weight / 2 > current_sum:
            wm = pair[value]
            break

        current_sum += pair[weight]

    return wm
