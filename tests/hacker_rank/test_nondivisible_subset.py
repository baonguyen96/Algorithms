from src.hacker_rank.nondivisible_subset import count_subset_not_divisible_by_k
from tests.unit_test_template import UnitTestTemplate


class NonDivisibleSubSetTest(UnitTestTemplate):

    def test_count_subset_not_divisible_by_k_none(self):
        arr = [1, 7, 2, 4]
        k = 1
        expected = 0
        actual = count_subset_not_divisible_by_k(arr, k)
        self.assertEqual(expected, actual)

    def test_count_subset_not_divisible_by_k_single_odd(self):
        arr = [1, 2, 4, 6, 8]
        k = 2
        expected = 1
        actual = count_subset_not_divisible_by_k(arr, k)
        self.assertEqual(expected, actual)

    def test_count_subset_not_divisible_by_k_short(self):
        arr = [1, 7, 2, 4]
        k = 3
        expected = 3
        actual = count_subset_not_divisible_by_k(arr, k)
        self.assertEqual(expected, actual)

    def test_count_subset_not_divisible_by_k_long(self):
        arr = [278, 576, 496, 727, 410, 124, 338, 149, 209, 702, 282, 718, 771, 575, 436]
        k = 7
        expected = 11
        actual = count_subset_not_divisible_by_k(arr, k)
        self.assertEqual(expected, actual)
