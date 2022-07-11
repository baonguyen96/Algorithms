import src.introduction_to_algorithm_3e.chapter4.monge_array as ma
from tests.unit_test_template import UnitTestTemplate


class MongeArrayTest(UnitTestTemplate):
    def test_is_monge_array_brute_force_small(self):
        array = [[1, 1],
                 [1, 1]]
        self.assertTrue(ma.is_monge_array_brute_force(array))

        array = [[1, 1],
                 [2, 1]]
        self.assertTrue(ma.is_monge_array_brute_force(array))

        array = [[4, 1],
                 [2, 1]]
        self.assertFalse(ma.is_monge_array_brute_force(array))

    def test_is_monge_array_brute_force_large(self):
        array = [[10, 17, 13, 28, 23],
                 [17, 22, 16, 29, 23],
                 [24, 28, 22, 34, 24],
                 [11, 13, 6, 17, 7],
                 [45, 44, 32, 37, 23],
                 [36, 33, 19, 21, 6],
                 [75, 66, 51, 53, 34]]
        self.assertTrue(ma.is_monge_array_brute_force(array))

        array = [[37, 23, 22, 32],
                 [21, 6, 7, 10],
                 [53, 34, 30, 31],
                 [32, 13, 9, 6],
                 [43, 21, 15, 8]]
        self.assertFalse(ma.is_monge_array_brute_force(array))
