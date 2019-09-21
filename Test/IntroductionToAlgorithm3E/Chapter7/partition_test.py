from IntroductionToAlgorithm3E.Chapter7.partition import partition, random_partition
from Test.unit_test_template import UnitTestTemplate


class PartitionTest(UnitTestTemplate):
    def test_parititon_single(self):
        array = [1]
        pivot = partition(array, 0, 0)
        self.assertEqual([1], array)
        self.assertTrue(0, pivot)

    def test_parititon(self):
        array = [2, 8, 7, 1, 3, 5, 6, 4]
        pivot = partition(array)
        self.assertEqual([2, 1, 3, 4, 7, 5, 6, 8], array)
        self.assertTrue(4, pivot)

        pv_index = array.index(pivot)
        for i in range(pv_index):
            self.assertTrue(array[i] < pv_index)
        for i in range(pv_index + 1, len(array)):
            self.assertTrue(array[i] > pv_index)
