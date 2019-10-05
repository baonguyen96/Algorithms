"""
Count Negative Integers in Row/Column-Wise Sorted Matrix
"""


def count_negative_elements_in_matrix(matrix):
    rows = len(matrix)
    columns = len(matrix[0])

    if matrix[0][0] >= 0:
        return 0

    if matrix[rows - 1][columns - 1] < 0:
        return rows * columns

    total_negatives = 0
    last_negative_column = columns - 1

    for r in range(rows):
        for c in range(last_negative_column, -1, -1):
            if matrix[r][c] < 0:
                last_negative_column = c
                total_negatives += c + 1
                break

        if last_negative_column < 0:
            break

    return total_negatives
