import src.src.introduction_to_algorithm_3e.chapter4.max_subarray as ms
from src.utilities.utility import get_random_array
from tests.unit_test_template import UnitTestTemplate


class MaxSubArrayTest(UnitTestTemplate):

    def test_find_max_sub_array_brute_force(self):
        array = [-6, -1, 2, 3, -18, -18, -19, -8, 6, -16, -16, 1, 10, -14, 1, -15, -16, 11, -13, 11]
        low, high, max_sum = ms.find_max_sub_array_brute_force(array)
        self.assertEqual(11, low)
        self.assertEqual(12, high)
        self.assertEqual(11, max_sum)

    def test_find_max_sub_array_linear(self):
        array = [-6, -1, 2, 3, -18, -18, -19, -8, 6, -16, -16, 1, 10, -14, 1, -15, -16, 11, -13, 11]
        low, high, max_sum = ms.find_max_sub_array_linear(array)
        self.assertEqual(11, low)
        self.assertEqual(12, high)
        self.assertEqual(11, max_sum)

    def test_find_max_sub_array_brute_force_all_positive(self):
        array = [1, 2, 3, 4]
        low, high, max_sum = ms.find_max_sub_array_brute_force(array)
        self.assertEqual(0, low)
        self.assertEqual(3, high)
        self.assertEqual(10, max_sum)

    def test_find_max_sub_array_linear_all_positive(self):
        array = [1, 2, 3, 4]
        low, high, max_sum = ms.find_max_sub_array_linear(array)
        self.assertEqual(0, low)
        self.assertEqual(3, high)
        self.assertEqual(10, max_sum)

    def test_find_max_sub_array_brute_force_all_negative(self):
        array = [-1, -2, -3, -4]
        low, high, max_sum = ms.find_max_sub_array_brute_force(array)
        self.assertEqual(0, low)
        self.assertEqual(0, high)
        self.assertEqual(-1, max_sum)

    def test_find_max_sub_array_linear_all_negative(self):
        array = [-1, -2, -3, -4]
        low, high, max_sum = ms.find_max_sub_array_linear(array)
        self.assertEqual(0, low)
        self.assertEqual(0, high)
        self.assertEqual(-1, max_sum)

    def test_find_max_sub_array_brute_force_performance_only(self):
        array = get_random_array(10000, -100, 100)
        ms.find_max_sub_array_brute_force(array)
        self.assertTrue(True)

    def test_find_max_sub_array_linear_performance_only(self):
        array = get_random_array(10000, -100, 100)
        ms.find_max_sub_array_linear(array)
        self.assertTrue(True)
