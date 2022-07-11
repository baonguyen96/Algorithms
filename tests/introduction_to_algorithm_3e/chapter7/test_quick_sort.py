from random import shuffle

import src.introduction_to_algorithm_3e.chapter7.quick_sort as qs
from tests.unit_test_template import UnitTestTemplate


class QuickSortTest(UnitTestTemplate):
    def test_quick_sort_small(self):
        array = [1, 2, 3, 4, 5]
        qs.quick_sort(array)
        self.assertEqual([1, 2, 3, 4, 5], array)

        shuffle(array)
        qs.quick_sort(array)
        self.assertEqual([1, 2, 3, 4, 5], array)

    def test_quick_sort_random_small(self):
        array = [1, 2, 3, 4, 5]
        qs.quick_sort_random(array)
        self.assertEqual([1, 2, 3, 4, 5], array)

        shuffle(array)
        qs.quick_sort_random(array)
        self.assertEqual([1, 2, 3, 4, 5], array)

    def test_quick_sort_big_sorted(self):
        array = list(range(10000))
        with self.assertRaises(RecursionError):
            qs.quick_sort(array)

    def test_quick_sort_random_big_sorted(self):
        array = list(range(10000))
        qs.quick_sort_random(array)
        self.assertEqual(list(range(10000)), array)

    def test_quick_sort_random_duplicated(self):
        array = list(range(1, 10)) * 2
        qs.quick_sort_random(array)
        expected_array = sorted(list(range(1, 10)) * 2)
        self.assertEqual(expected_array, array)

