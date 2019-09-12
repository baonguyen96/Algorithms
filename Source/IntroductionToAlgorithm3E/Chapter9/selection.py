"""
Selection problem:
    Input: A set A of n (distinct) numbers and an integer i , with 1 <= i <= n.
    Output: The element x in A that is larger than exactly i - 1 other elements of A.
"""


def select_brute_force(array, i):
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
    if len(array) == 1:
        return array[0]

    array.sort()
    return array[i]


def select_linear(array, i):
    pass
