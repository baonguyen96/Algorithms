from random import shuffle

from src.introduction_to_algorithm_3e.chapter9.closest_to_median import find_k_elements_closest_to_median
from tests.unit_test_template import UnitTestTemplate


class ClosestToMedianTest(UnitTestTemplate):
    def test_find_k_elements_closest_to_median_none(self):
        array = []
        k = 0
        expected = []
        actual = find_k_elements_closest_to_median(array, k)
        self.assertEqual(expected, actual)

    def test_find_k_elements_closest_to_median_even_k(self):
        array = list(range(10))
        shuffle(array)
        k = 2
        expected = [4, 6]
        actual = find_k_elements_closest_to_median(array, k)
        self.assertEqual(expected, actual)

        array = list(range(11))
        shuffle(array)
        actual = find_k_elements_closest_to_median(array, k)
        self.assertEqual(expected, actual)

        array = list(range(9))
        shuffle(array)
        k = 8
        expected = [0, 1, 2, 3, 5, 6, 7, 8]
        actual = find_k_elements_closest_to_median(array, k)
        self.assertEqual(set(expected), set(actual))

    def test_find_k_elements_closest_to_median_odd_k(self):
        array = list(range(10))
        k = 1
        expected = [4]
        actual = find_k_elements_closest_to_median(array, k)
        self.assertEqual(expected, actual)

        shuffle(array)
        k = 3
        expected = [3, 4, 6]
        actual = find_k_elements_closest_to_median(array, k)
        self.assertEqual(set(expected), set(actual))

        shuffle(array)
        k = 5
        expected = [2, 3, 4, 6, 7]
        actual = find_k_elements_closest_to_median(array, k)
        self.assertEqual(expected, actual)

        array = list(range(9))
        k = 1
        expected = [3]
        actual = find_k_elements_closest_to_median(array, k)
        self.assertEqual(expected, actual)
