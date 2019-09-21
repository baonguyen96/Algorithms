from random import shuffle

from IntroductionToAlgorithm3E.Chapter7.partition import partition, random_partition
from Test.unit_test_template import UnitTestTemplate


class PartitionTest(UnitTestTemplate):
    def test_parititon_single(self):
        array = [1]
        pivot_index = partition(array, 0, 0)
        self.assertEqual([1], array)
        self.assertEqual(1, array[pivot_index])
        self.assertEqual(0, pivot_index)

    def test_parititon_small_list(self):
        array = [2, 8, 7, 1, 3, 5, 6, 4]
        pv_index = partition(array)
        self.assertEqual([2, 1, 3, 4, 7, 5, 6, 8], array)
        self.assertTrue(4, array[pv_index])

        for i in range(pv_index - 1):
            self.assertTrue(array[i] < array[pv_index])
        for i in range(pv_index + 1, len(array)):
            self.assertTrue(array[i] > array[pv_index])

    def test_parititon_big_list(self):
        array = list(range(1000))
        expected_pivot = array[len(array) - 1]
        pv_index = partition(array)
        self.assertTrue(expected_pivot, array[pv_index])

        for i in range(pv_index - 1):
            self.assertTrue(array[i] < array[pv_index])
        for i in range(pv_index + 1, len(array)):
            self.assertTrue(array[i] > array[pv_index])

    def test_random_partition_sub_list(self):
        array = list(range(1000))
        shuffle(array)
        expected_pivot = array[10]
        pv_index = random_partition(array, 0, 10)
        self.assertTrue(expected_pivot, array[pv_index])

        for i in range(pv_index - 1):
            self.assertTrue(array[i] < array[pv_index])
        for i in range(pv_index + 1, 10):
            self.assertTrue(array[i] > array[pv_index])

    def test_random_parititon_big_list(self):
        array = list(range(1000))
        pv_index = partition(array)

        for i in range(pv_index - 1):
            self.assertTrue(array[i] < array[pv_index])
        for i in range(pv_index + 1, len(array)):
            self.assertTrue(array[i] > array[pv_index])
