from random import shuffle

from IntroductionToAlgorithm3E.Chapter9.closest_to_median import find_k_elements_closest_to_median
from Test.unit_test_template import UnitTestTemplate


class ClosestToMedianTest(UnitTestTemplate):
    def test_find_k_elements_closest_to_median_none(self):
        array = []
        k = 0
        expected = []
        actual = find_k_elements_closest_to_median(array, k)
        self.assertEqual(expected, actual)

    def test_find_k_elements_closest_to_median_even(self):
        array = list(range(10))
        k = 2
        expected = [4, 6]
        actual = find_k_elements_closest_to_median(array, k)
        self.assertEqual(expected, actual)

        shuffle(array)
        actual = find_k_elements_closest_to_median(array, k)
        self.assertEqual(expected, actual)

    def test_find_k_elements_closest_to_median_odd(self):
        array = list(range(10))
        k = 1
        expected = [4]
        actual = find_k_elements_closest_to_median(array, k)
        self.assertEqual(expected, actual)

        shuffle(array)
        k = 3
        expected = [3, 4, 6]
        actual = find_k_elements_closest_to_median(array, k)
        self.assertEqual(expected, actual)
