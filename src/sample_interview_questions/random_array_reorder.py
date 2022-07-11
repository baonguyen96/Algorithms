"""
Randomly reorder an array in O(n) time
"""
import random
from math import floor


def reorder(array):
    for i in range(len(array)):
        rand = random.random()
        new_index = floor(len(array) * rand)
        array[i], array[new_index] = array[new_index], array[i]

    return array
