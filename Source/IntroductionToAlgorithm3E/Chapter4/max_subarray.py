"""
Problem 4.1-5

Use the following ideas to develop a nonrecursive, linear-time algorithm for the
maximum-subarray problem. Start at the left end of the array, and progress toward
the right, keeping track of the maximum subarray seen so far. Knowing a maximum
subarray of A[1...j], extend the answer to find a maximum subarray ending at index
j + 1 by using the following observation: a maximum subarray of A[1...j + 1]
is either a maximum subarray of A[1...j] or a subarray A[1...j + 1], for some
1 <= i <= j + 1. Determine a maximum subarray of the form A[1...j + 1] in
constant time based on knowing a maximum subarray ending at index j .

Maximum subarray problem: https://en.wikipedia.org/wiki/Maximum_subarray_problem
"""


def find_max_brute_force(array):
    if array is None or len(array) == 0:
        return 0, 0, 0

    global_max_sum = array[0]
    low = 0
    high = 0

    for i in range(0, len(array)):
        local_max_sum = array[i]

        for j in range(i, len(array)):
            if i != j:
                local_max_sum += array[j]

            if local_max_sum > global_max_sum:
                low = i
                high = j
                global_max_sum = local_max_sum

    return low, high, global_max_sum


def find_max_linear(array):
    if array is None or len(array) == 0:
        return 0, 0, 0

    global_max_sum = array[0]
    local_sum = array[0]
    low = 0
    high = 0
    temp_low = 0

    for i in range(1, len(array)):
        local_sum += array[i]

        if array[i] > local_sum:
            local_max_sum = array[i]
            local_sum = array[i]
            temp_low = i
        else:
            local_max_sum = local_sum

        if local_max_sum > global_max_sum:
            global_max_sum = local_max_sum
            high = i
            low = temp_low

    return low, high, global_max_sum
