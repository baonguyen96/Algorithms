from IntroductionToAlgorithm3E.Chapter7.partition import partition, random_partition
from Test.unit_test_template import UnitTestTemplate


class PartitionTest(UnitTestTemplate):
    def test_parititon(self):
        array = [2, 8, 7, 1, 3, 5, 6, 4]
        pivot = partition(array)
        self.assertEqual([2, 1, 3, 4, 7, 5, 6, 8], array)
        self.assertTrue(4, pivot)
