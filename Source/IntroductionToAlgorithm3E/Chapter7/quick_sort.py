from IntroductionToAlgorithm3E.Chapter7.partition import partition


def quick_sort(array):
    _quick_sort(array, 0, len(array) - 1)


def _quick_sort(array, low, high):
    if low < high:
        pv = partition(array, low, high)
        _quick_sort(array, low, pv - 1)
        _quick_sort(array, pv + 1, high)
