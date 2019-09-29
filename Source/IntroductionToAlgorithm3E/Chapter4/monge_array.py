"""
Problem 4.6

An m x n array A of real numbers is a Monge array if for all i , j , k, and l
    such that 1 <= i < k <= m and 1 <= j < l <= n,
    we have A[i][j] + A[k][l] <= A[i, l] + A[k, j].
    In other words, whenever we pick two rows and two columns of a Monge array
    and consider the four elements at the intersections of the rows and the columns,
    the sum of the upper-left and lower-right elements is less than or equal to
    the sum of the lower-left and upper-right elements.
"""


def is_monge_array_brute_force(array):
    rows = len(array)
    cols = len(array[0])

    for row in range(rows):
        for row_diff in range(row + 1, rows - row):
            for col in range(cols):
                for col_diff in range(col + 1, cols - col):
                    upper_left = array[row][col]
                    upper_right = array[row][col_diff]
                    lower_left = array[row_diff][col]
                    lower_right = array[row_diff][col_diff]

                    if upper_left + lower_right > upper_right + lower_left:
                        return False

    return True
