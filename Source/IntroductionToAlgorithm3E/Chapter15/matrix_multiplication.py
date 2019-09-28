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


