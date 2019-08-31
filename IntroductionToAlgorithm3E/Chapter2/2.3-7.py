"""
Problem 2.3-7
Describe a O(nlogn)-time algorithm that,
    given a set S of n integers and another integer x,
    determines whether or not there exist two elements in S
    whose sum is exactly x.
"""
from Utitilies.utility import binary_search


def exist_elements_with_sum(s, x):
    s.sort()
    found = False

    for i in s:
        j = x - i

        if binary_search(s, j) > -1:
            found = True
            break

    return found


def main():
    aray = [2, 5, 1, 4]
    expected_sum = 1
    exist = exist_elements_with_sum(aray, expected_sum)

    print(aray)
    print(expected_sum)
    print(exist)


main()
