"""
Given two sequences X and Y , we say that a sequence Z is a common subsequence
    of X and Y if Z is a subsequence of both X and Y.
    In the longest-common-subsequence problem, we are given two sequences X and Y
    and wish to find a maximum length common subsequence of X and Y.
"""


def find_longest_common_subsequence(x, y):
    # force additional first row and column
    x = [None] + x
    y = [None] + y
    common_lengths = [[0 for j in range(len(y))] for i in range(len(x))]

    for i in range(1, len(x)):
        for j in range(1, len(y)):
            if x[i] == y[j]:
                common_lengths[i][j] = common_lengths[i - 1][j - 1] + 1
            else:
                common_lengths[i][j] = max(common_lengths[i][j - 1], common_lengths[i - 1][j])

    # reset x and y + remove additional first row and column
    x = x[1:]
    y = y[1:]
    [r.pop(0) for r in common_lengths]
    common_lengths.pop(0)

    return reconstruct_longest_common_subsequence(x, y, common_lengths)


def reconstruct_longest_common_subsequence(x, y, common_lengths):
    longest_sequence_reversed = []
    i = len(x) - 1
    j = len(y) - 1

    while i >= 0 and j >= 0:
        if x[i] == y[j]:
            longest_sequence_reversed += [x[i]]

        # go left
        if common_lengths[i - 1][j] < common_lengths[i][j - 1]:
            j -= 1
        # go up
        elif common_lengths[i - 1][j] == common_lengths[i][j]:
            i -= 1
        # go top left
        else:
            i -= 1
            j -= 1

    longest_sequence_reversed.reverse()
    return longest_sequence_reversed
