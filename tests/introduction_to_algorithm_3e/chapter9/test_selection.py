import unittest

from src.introduction_to_algorithm_3e.chapter9.selection import select_using_sort, select_brute_force, select_partition
from tests.unit_test_template import UnitTestTemplate


class SelectionTest(UnitTestTemplate):
    def test_select_brute_force_single(self):
        array = [1]
        x = select_brute_force(array, 1)
        self.assertEqual(1, x)

    def test_select_sort_single(self):
        array = [1]
        x = select_using_sort(array, 1)
        self.assertEqual(1, x)

    def test_select_random_partition_single(self):
        array = [1]
        x = select_partition(array, 1)
        self.assertEqual(1, x)

    def test_select_brute_force_small_list(self):
        array = [1, 2, 3, 4, 5]
        x = select_brute_force(array, 2)
        self.assertEqual(3, x)

        array = [5, 4, 3, 2, 1]
        x = select_brute_force(array, 3)
        self.assertEqual(4, x)

    def test_select_sort_small_list(self):
        array = [1, 2, 3, 4, 5]
        x = select_using_sort(array, 2)
        self.assertEqual(3, x)

        array.reverse()
        x = select_using_sort(array, 3)
        self.assertEqual(4, x)

    def test_select_partition_small_list(self):
        array = [0]
        x = select_partition(array, 1)
        self.assertEqual(0, x)

        array = [1, 2, 3, 4, 5]
        x = select_partition(array, 2)
        self.assertEqual(3, x)

        array = [5, 7, 6, 8, 9, 10]
        x = select_partition(array, 1)
        self.assertEqual(6, x)

    def test_select_brute_force_big_list(self):
        array = list(range(1001))
        x = select_brute_force(array, 10)
        self.assertEqual(10, x)

        x = select_brute_force(array, 1000)
        self.assertEqual(1000, x)

    def test_select_sort_big_list(self):
        array = list(range(1001))
        x = select_using_sort(array, 10)
        self.assertEqual(10, x)

        x = select_using_sort(array, 1000)
        self.assertEqual(1000, x)

    def test_select_partition_big_list(self):
        array = list(range(1001))
        x = select_partition(array, 10)
        self.assertEqual(10, x)

        x = select_partition(array, 1000)
        self.assertEqual(1000, x)
