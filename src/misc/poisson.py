"""
When using iterative methods, the matrices are typically very sparse.
The question then is how to store a sparse matrix and how to perform a matrix-vector multiplication with it.
One popular way is known as compressed row storage that involves three arrays:
    1D array nzA (nonzero A) which stores the nonzero elements of matrix A.
        In this array, first all nonzero elements of the first row are stored, then the second row, etc.
        It has size nnzeroes (number of nonzeroes).

    1D array ir which is an integer array of size n + 1 such that ir( 1 ) equals the index in array nzA where the first element of the first row is stored. ir( 2 ) then gives the index where the first element of the second row is stored, and so forth. ir( n+1 ) equals nnzeroes + 1.
        Having this entry is convenient when you implement a matrix-vector multiplication with array nzA.

    1D array ic of size nnzeroes which holds the column indices of the corresponding elements in array nzA.

Write a function [ nzA, ir, ic ] = Create_Poisson_problem_nzA(N) that creates the matrix A in this sparse format.

Write a function y = SparseMvMult( nzA, ir, ic, x ) that computes y=Ax with the matrix A stored in the sparse format.
"""
import random


def create_poisson_problem_nza(n):
    if n <= 0:
        return [], [], []

    if n == 1:
        return [4], [0, 1], [0]

    nza = compute_nza(n)
    flat_nza = [item for sublist in nza for item in sublist]

    ir = compute_ir(nza)
    assert len(ir) == n**2 + 1

    ic = compute_ic(n)
    assert len(ic) == len(flat_nza)

    return flat_nza, ir, ic


def compute_nza(n):
    nza, tmp = [], []

    for block in range(n):
        for row in range(n):
            # main block
            if row == 0:
                tmp = [4, -1]
            elif row == n - 1:
                tmp = [-1, 4]
            else:
                tmp = [-1, 4, -1]

            # neighbor blocks
            if block == 0:
                tmp += [-1]
            elif block == n - 1:
                tmp = [-1] + tmp
            else:
                tmp = [-1] + tmp + [-1]

            # print(f'block {block}: row {row}: {tmp}')
            nza += [tmp]

    return nza


def compute_ir(nza):
    ir = []
    agg_len = 1

    for row in nza:
        ir += [agg_len]
        agg_len += len(row)

    ir += [agg_len]
    return ir


def compute_ic(n):
    ic, tmp = [], []

    for block in range(n):
        for row in range(n):
            block_start_index = block * n

            # main block
            if row == 0:
                tmp = [block_start_index, block_start_index + 1]
            elif row == n - 1:
                tmp = [n - 2 + block_start_index, n - 1 + block_start_index]
            else:
                tmp = [row - 1 + block_start_index, row + block_start_index, row + 1 + block_start_index]

            # neighbor blocks
            if block == 0:
                tmp += [n + row]
            elif block == n - 1:
                tmp = [n * (n - 2) + row] + tmp
            else:
                tmp = [(block - 1) * n + row] + tmp + [(block + 1) * n + row]

            # print(f'block {block}: row {row}: {tmp}')
            ic += tmp

    # offset by 1
    ic = [e + 1 for e in ic]
    return ic


def sparse_mv_mult(nza, ir, ic, x):
    y = []

    assert max(ic) == len(x)
    exploded_x = [x[i - 1] for i in ic]
    # print(f'x = {x}')
    # print(f'exploded_x = {exploded_x}')
    assert len(nza) == len(exploded_x)

    # offset by 1
    ir = [i - 1 for i in ir]
    tmp = 0

    for i in range(len(nza)):
        tmp += nza[i] * exploded_x[i]

        if i == 0:
            continue

        if i + 1 in ir:
            y += [tmp]
            tmp = 0

    assert len(y) == len(x)
    return y


def main():
    n = 2
    x = [random.randint(1, 10) for _ in range((n ** 2))]
    print(f'n = {n}')
    print(f'x = {x}')
    print()

    nza, ir, ic = create_poisson_problem_nza(n)
    print(f'nza = {nza}')
    print(f'ir = {ir}')
    print(f'ic = {ic}')
    print()

    y = sparse_mv_mult(nza, ir, ic, x)
    print(f'y = {y}')


if __name__ == '__main__':
    main()
