import random


def partition(array, low=None, high=None):
    if low is None and high is None:
        return partition(array, 0, len(array) - 1)
    else:
        pivot = array[high]
        i = low - 1

        for j in range(low, high):
            if array[j] <= pivot:
                i = i + 1
                array[i], array[j] = array[j], array[i]

        array[i + 1], array[high] = array[high], array[i + 1]
        return i + 1


def random_partition(array, low=None, high=None):
    if low is None and high is None:
        return random_partition(array, 0, len(array) - 1)
    else:
        i = random.randint(low, high)
        array[i], array[high] = array[high], array[i]
        return partition(array, low, high)
