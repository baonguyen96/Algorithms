import IntroductionToAlgorithm3E.Chapter15.matrix_multiplication as mat
from Test.unit_test_template import UnitTestTemplate
import Utitilies.utility as util


class MatrixMultiplicationTest(UnitTestTemplate):
    def test_multiply_incompatible(self):
        matrix_a = [[1, 2, 3],
                    [4, 5, 6]]
        matrix_b = [[1, 2, 3],
                    [4, 5, 6]]
        with self.assertRaises(Exception):
            mat.multiply_matrices(matrix_a, matrix_b)

    def test_multiply_matrices(self):
        matrix_a = [[1, 2, 3],
                    [4, 5, 6]]
        matrix_b = [[7, 8],
                    [9, 10],
                    [11, 12]]
        expected_matrix_c = [[58, 64],
                             [139, 154]]
        actual_matrix_c = mat.multiply_matrices(matrix_a, matrix_b)
        self.assertEqual(expected_matrix_c, actual_matrix_c)

    def test_multiply_n_matrices(self):
        matrix_a = [[1, 2, 3],
                    [4, 5, 6]]
        matrix_b = [[7, 8],
                    [9, 10],
                    [11, 12]]
        matrix_c = [[1, 0],
                    [0, 1]]
        matrices = [matrix_a, matrix_b, matrix_c]
        expected_matrix_d = [[58, 64],
                             [139, 154]]
        actual_matrix_d = mat.multiply_n_matrices(matrices)
        self.assertEqual(expected_matrix_d, actual_matrix_d)

        matrices = [util.get_identity_matrix_with_dimension(2),
                    util.get_identity_matrix_with_dimension(2),
                    util.get_identity_matrix_with_dimension(3)]
        with self.assertRaises(Exception):
            mat.multiply_n_matrices(matrices)

    def test_find_optimal_matrix_chain_order(self):
        matrix_a0 = util.get_default_matrix_with_dimension(5, 5)
        matrix_a1 = util.get_default_matrix_with_dimension(5, 3)
        matrix_a2 = util.get_default_matrix_with_dimension(3, 4)
        matrix_a3 = util.get_default_matrix_with_dimension(4, 2)
        matrix_a4 = util.get_default_matrix_with_dimension(2, 3)
        matrices = [matrix_a0, matrix_a1, matrix_a2, matrix_a3, matrix_a4]

        dimensions = []
        for matrix in matrices:
            dimensions += [len(matrix)]
        dimensions += [len(matrices[len(matrices) - 1][0])]

        matrix_costs, matrix_splits = mat.find_optimal_matrix_chain_order(dimensions)
        self.assertEqual(5, len(matrix_costs))
        self.assertEqual(5, len(matrix_costs[0]))
        self.assertEqual(5, len(matrix_splits))
        self.assertEqual(5, len(matrix_splits[0]))

        expected_matrix_splits = [[None, 0, 1, 0, 3],
                                  [None, None, 1, 1, 3],
                                  [None, None, None, 2, 3],
                                  [None, None, None, None, 3],
                                  [None, None, None, None, None]]
        self.assertEqual(expected_matrix_splits, matrix_splits)

        expected_matrix_costs = [[0, 75, 135, 104, 134],
                                 [None, 0, 60, 54, 84],
                                 [None, None, 0, 24, 42],
                                 [None, None, None, 0, 24],
                                 [None, None, None, None, 0]]
        self.assertEqual(expected_matrix_costs, matrix_costs)

    def test_get_optimal_chain_as_string(self):
        splits = [[None, 0, 1, 0, 3],
                  [0, None, 1, 1, 3],
                  [0, 0, None, 2, 3],
                  [0, 0, 0, None, 3],
                  [0, 0, 0, 0, None]]

        s = mat.get_optimal_chain_as_string(splits, 0, 4)
        self.assertEqual('((A0(A1(A2A3)))A4)', s)
