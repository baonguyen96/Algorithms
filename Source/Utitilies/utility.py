import random


def get_random_array(size, low, high):
    array = []

    for i in range(size):
        array += [random.randint(low, high)]

    return array


def binary_search(array, element):
    low = 0
    high = len(array) - 1

    while low <= high:
        mid = (low + high) // 2

        if array[mid] == element:
            return mid
        elif array[mid] > element:
            high = mid - 1
        else:
            low = mid + 1

    return -1


def is_even(n):
    return n % 2 == 0


def get_difference(x, y):
    return abs(x - y)


def get_all_binaries_for_length(length):
    rows = 2 ** length
    columns = length
    bits = [[False for c in range(columns)] for r in range(rows)]

    for c in range(columns - 1, -1, -1):
        count = 0
        group = 2 ** (columns - c - 1)
        current_flag = False

        for r in range(rows):
            bits[r][c] = current_flag
            count += 1

            if count == group:
                current_flag = not current_flag
                count = 0

    return bits
