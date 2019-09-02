"""
Problem 2.4
Give an algorithm that determines the number of inversions in any permutation on n elements in O(nlogn) worst-case time

Inversion definition: https://en.wikipedia.org/wiki/Inversion
"""


def count_inversion_brute_force(array):
    inversion_count = 0

    for i in range(len(array) - 1):
        for j in range(i, len(array)):
            if array[i] > array[j]:
                inversion_count += 1

    return inversion_count


def count_inversion_using_merge_sort(array):
    inversion_count = 0

    if len(array) <= 1:
        return 0
    else:
        mid = len(array) // 2
        left_array = array[:mid]
        right_array = array[mid:]

        inversion_count += count_inversion_using_merge_sort(left_array)
        inversion_count += count_inversion_using_merge_sort(right_array)

        left_index = 0
        right_index = 0
        array_index = 0
        right_array_max_element = right_array[0]

        while left_index < len(left_array) and right_index < len(right_array):
            if right_array[right_index] > right_array_max_element:
                right_array_max_element = right_array[right_index]

            if left_array[left_index] < right_array[right_index]:
                if left_index < right_index:
                    inversion_count += 1
                array[array_index] = left_array[left_index]
                left_index = left_index + 1
            else:
                array[array_index] = right_array[right_index]
                right_index = right_index + 1
            array_index = array_index + 1

        while left_index < len(left_array):
            if left_array[left_index] > right_array_max_element:
                inversion_count += 1

            array[array_index] = left_array[left_index]
            left_index = left_index + 1
            array_index = array_index + 1

        while right_index < len(right_array):
            array[array_index] = right_array[right_index]
            right_index = right_index + 1
            array_index = array_index + 1

        return inversion_count
