"""
Find all possible permutations of a string.
"""


def get_all_permutation(string):
    if string is None or len(string) == 0:
        return None

    permutations = []
    permute(list(string), 0, len(string) - 1, permutations)

    return permutations


def permute(array, left, right, permutations):
    if left == right:
        permutations += [''.join(array)]
    else:
        for i in range(left, right + 1):
            array[left], array[i] = array[i], array[left]
            permute(array, left + 1, right, permutations)
            array[left], array[i] = array[i], array[left]
