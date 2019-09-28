import Source.Utitilies.utility as util
from Test.unit_test_template import UnitTestTemplate


class UtilityTest(UnitTestTemplate):

    def test_get_random_array(self):
        array = util.get_random_array(10, -10, 10)
        array.sort()
        self.assertEqual(len(array), 10)
        self.assertTrue(array[0] >= -10)
        self.assertTrue(array[9] <= 10)

    def test_binary_search(self):
        array = [-1, 0, 1, 2, 3]
        self.assertEqual(0, util.binary_search(array, -1))
        self.assertEqual(1, util.binary_search(array, 0))
        self.assertEqual(-1, util.binary_search(array, 9))

    def test_get_identity_matrix(self):
        identity_matrix = util.get_identity_matrix_with_dimension(1)
        expectected_identity_matrix = [[1]]
        self.assertEqual(expectected_identity_matrix, identity_matrix)

        identity_matrix = util.get_identity_matrix_with_dimension(2)
        expectected_identity_matrix = [[1, 0],
                                       [0, 1]]
        self.assertEqual(expectected_identity_matrix, identity_matrix)

        identity_matrix = util.get_identity_matrix_with_dimension(3)
        expectected_identity_matrix = [[1, 0, 0],
                                       [0, 1, 0],
                                       [0, 0, 1]]
        self.assertEqual(expectected_identity_matrix, identity_matrix)

    def test_get_default_matrix_with_dimension(self):
        matrix = [[0]]
        expected_matrix = util.get_default_matrix_with_dimension(1, 1)
        self.assertEqual(expected_matrix, matrix)

        matrix = [[0, 0], [0, 0], [0, 0]]
        expected_matrix = util.get_default_matrix_with_dimension(3, 2)
        self.assertEqual(expected_matrix, matrix)
