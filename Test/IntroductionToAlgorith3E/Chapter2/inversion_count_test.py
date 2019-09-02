import Source.IntroductionToAlgorithm3E.Chapter2.inversion_count as ic
from Source.Utitilies.utility import get_random_array
from Test.unit_test_template import UnitTestTemplate


class InversionCountTest(UnitTestTemplate):

    def test_count_inversion_empty(self):
        array = []
        count = ic.count_inversion_brute_force(array)
        self.assertEqual(0, count)

        count = ic.count_inversion_using_merge_sort(array)
        self.assertEqual(0, count)

    def test_count_inversion_none(self):
        array = [1, 2, 3]
        count = ic.count_inversion_brute_force(array)
        self.assertEqual(0, count)

        array = [1, 2, 3]
        count = ic.count_inversion_using_merge_sort(array)
        self.assertEqual(0, count)

    def test_count_inversion_all(self):
        array = [3, 2, 1]
        count = ic.count_inversion_brute_force(array)
        self.assertEqual(3, count)

        array = [3, 2, 1]
        count = ic.count_inversion_brute_force(array)
        self.assertEqual(3, count)

    def test_count_inversion_small_array(self):
        array = [1, 5, 6, 4, 20, -1]
        count = ic.count_inversion_brute_force(array)
        self.assertEqual(7, count)

        array = [1, 5, 6, 4, 20, -1]
        count = ic.count_inversion_brute_force(array)
        self.assertEqual(7, count)

    def test_count_inversion_large_array_brute_force_performance_only(self):
        array = get_random_array(10000, -100, 100)
        ic.count_inversion_brute_force(array)
        self.assertTrue(True)

    def test_count_inversion_large_array_merge_sort_performance_only(self):
        array = get_random_array(10000, -100, 100)
        ic.count_inversion_using_merge_sort(array)
        self.assertTrue(True)
