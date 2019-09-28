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


def get_identity_matrix(dim):
    matrix = [[0 for i in range(dim)] for j in range(dim)]

    for i in range(dim):
        matrix[i][i] = 1

    return matrix


def get_default_matrix_with_dimension(rows, columns):
    matrix = [[0 for c in range(columns)] for r in range(rows)]
    return matrix
