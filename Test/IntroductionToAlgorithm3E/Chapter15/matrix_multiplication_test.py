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

        matrices = [util.get_identity_matrix(2), util.get_identity_matrix(2), util.get_identity_matrix(3)]
        with self.assertRaises(Exception):
            mat.multiply_n_matrices(matrices)
