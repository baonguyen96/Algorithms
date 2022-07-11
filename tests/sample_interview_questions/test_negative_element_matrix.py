from src.sample_interview_questions.negative_element_matrix import count_negative_elements_in_matrix
from tests.unit_test_template import UnitTestTemplate


class NegativeElementMatrixTest(UnitTestTemplate):
    def test_count_negative_elements_in_matrix_none(self):
        matrix = [[1 for c in range(10)] for r in range(10)]
        count = count_negative_elements_in_matrix(matrix)
        self.assertEqual(0, count)

    def test_count_negative_elements_in_matrix_all(self):
        matrix = [[-1 for c in range(10)] for r in range(10)]
        count = count_negative_elements_in_matrix(matrix)
        self.assertEqual(100, count)

    def test_count_negative_elements_in_matrix_multiple(self):
        matrix = [[-3, -2, -1, 1],
                  [-2, 2, 3, 4],
                  [4, 5, 7, 8]]
        matrix += [[10 for c in range(4)] for r in range(1000)]
        count = count_negative_elements_in_matrix(matrix)
        self.assertEqual(4, count)

        matrix = [[-3, -2, -1, 1],
                  [-2, -1, 3, 4],
                  [-1, 5, 7, 8],
                  [0, 6, 9, 10]]
        count = count_negative_elements_in_matrix(matrix)
        self.assertEqual(6, count)
