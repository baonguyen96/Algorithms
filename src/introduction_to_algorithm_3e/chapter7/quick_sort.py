from introduction_to_algorithm_3e.chapter7.partition import partition, random_partition


def quick_sort(array):
    _quick_sort(array, 0, len(array) - 1)


def _quick_sort(array, low, high):
    if low < high:
        pv = partition(array, low, high)
        _quick_sort(array, low, pv - 1)
        _quick_sort(array, pv + 1, high)


def quick_sort_random(array):
    _quick_sort_random(array, 0, len(array) - 1)


def _quick_sort_random(array, low, high):
    if low < high:
        pv = random_partition(array, low, high)
        _quick_sort_random(array, low, pv - 1)
        _quick_sort_random(array, pv + 1, high)
