import random
import time


def get_random_array(size, low, high):
    array = []

    for i in range(size):
        array += [random.randint(low, high + 1)]

    return array


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


# a = [-6, -1, 2, 3, -18, -18, -19, -8, 6, -16, -16, 1, 10, -14, 1, -15, -16, 11, -13, 11]
# a = [6, -9, 5, 6, -2, 6, 11, 1, 7, 0]
# a = [-9, -8, -1, 11, -5, 11, -2, -2, 5, -9, 4, -8, 3, 7, -2, 11, 6, 1, 1, 6]
a = get_random_array(100000, -100, 100)

print(a)

start = time.time()
l, h, maxSum = find_max_linear(a)
end = time.time()
print('Linear: low = %d, high = %d, maxSum = %d' % (l, h, maxSum))
print('Complete in %s seconds' % (end - start))

start = time.time()
l, h, maxSum = find_max_brute_force(a)
end = time.time()
print('Brute force: low = %d, high = %d, maxSum = %d' % (l, h, maxSum))
print('Complete in %s seconds' % (end - start))
