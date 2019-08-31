"""
Problem 2.3-7
Describe a O(nlogn)-time algorithm that,
    given a set S of n integers and another integer x,
    determines whether or not there exist two elements in S
    whose sum is exactly x.
"""
import time

from Utitilies.utility import binary_search, get_random_array


def exist_elements_with_sum(s, x):
    s.sort()
    found = False

    for i in s:
        j = x - i

        if binary_search(s, j) > -1:
            found = True
            break

    return found


def main(array, expected_sum):
    start = time.time()

    print(array)
    print(expected_sum)
    exist = exist_elements_with_sum(array, expected_sum)

    end = time.time()
    print('NlogN: %s' % "Found" if exist else "Not found")
    print('Complete in %s seconds' % (end - start))
    print()


a = [2, 5, 1, 4]
main(a, 1)
main(a, 10)

a = get_random_array(1000, -20, 30)
main(a, 140)
main(a, a[0] + a[1])
