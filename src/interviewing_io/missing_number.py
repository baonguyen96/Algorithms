"""
https://interviewing.io/recordings/C++-Airbnb-2/

Given an unsorted array of unique integers (size n + 1) and a second array that is identical to the first array
    but missing one integer (size n), find and output the missing integer

"""


def get_missing_number(arr1, arr2):
    number_count = set()
    missing_number = None

    for i in arr2:
        number_count.add(i)

    for i in arr1:
        if i not in number_count:
            missing_number = i
            break

    return missing_number
