"""
Matrix multiplication

Matrix-chain multiplication problem: given a chain <A1, A2, ..., An> of n matrices,
    where for i = 1, 2, ..., n, matrix Ai has dimension p(i-1) * pi,
    fully parenthesize the product A1A2...An in a way that minimizes the
    number of scalar multiplications.
"""


def multiply_matrices(matrix_a, matrix_b):
    matrix_a_rows = len(matrix_a)
    matrix_a_cols = len(matrix_a[0])
    matrix_b_rows = len(matrix_b)
    matrix_b_cols = len(matrix_b[0])

    if matrix_a_cols != matrix_b_rows:
        raise Exception('Incompatible dimensions: [%d x %d] x [%d x %d]' %
                        (matrix_a_rows, matrix_a_cols, matrix_b_rows, matrix_b_cols))

    matrix_c = [[0 for j in range(matrix_b_cols)] for i in range(matrix_a_rows)]

    for i in range(matrix_a_rows):
        for j in range(matrix_b_cols):
            matrix_c[i][j] = 0
            for k in range(matrix_a_cols):
                matrix_c[i][j] = matrix_c[i][j] + matrix_a[i][k] * matrix_b[k][j]

    return matrix_c


def multiply_n_matrices(matrices):
    if matrices is None or len(matrices) == 0:
        raise Exception('No matrices to multiply')

    if len(matrices) == 1:
        return matrices[0]

    matrix_a = matrices[0]

    for b in list(range(1, len(matrices))):
        matrix_b = matrices[b]
        matrix_a = multiply_matrices(matrix_a, matrix_b)

    return matrix_a


# noinspection PyTypeChecker
def find_optimal_matrix_chain_order(dimensions):
    size = len(dimensions) - 1
    matrix_costs = [[None for c in range(size)] for r in range(size)]
    matrix_splits = [[None for c in range(size)] for r in range(size)]

    for i in range(size):
        for j in range(size):
            if i == j:
                matrix_costs[i][j] = 0
            elif i < j:
                matrix_costs[i][j] = float('inf')

    for length in range(1, size):
        for i in range(size - length):
            j = i + length

            for k in range(i + 1, j + 1):
                # print('length = %d, i = %d, k = %d, j = %d' % (length, i, k, j))

                scala = dimensions[i] * dimensions[k] * dimensions[j + 1]
                val = (matrix_costs[i][k - 1] + matrix_costs[k][j] if length > 1 else 0) + scala

                if val < matrix_costs[i][j]:
                    matrix_costs[i][j] = val
                    matrix_splits[i][j] = k - 1

    return matrix_costs, matrix_splits


def get_optimal_chain_as_string(splits, i, j):
    if i == j:
        return 'A%d' % i
    else:
        s = '('
        s += get_optimal_chain_as_string(splits, i, splits[i][j])
        s += get_optimal_chain_as_string(splits, splits[i][j] + 1, j)
        s += ')'
        return s
