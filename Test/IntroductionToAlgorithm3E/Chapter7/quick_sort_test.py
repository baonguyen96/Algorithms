from random import shuffle

from IntroductionToAlgorithm3E.Chapter7.quick_sort import quick_sort
from Test.unit_test_template import UnitTestTemplate


class QuickSortTest(UnitTestTemplate):
    def test_quick_sort(self):
        array = [1, 2, 3, 4, 5]
        quick_sort(array)
        self.assertEqual([1, 2, 3, 4, 5], array)

        shuffle(array)
        quick_sort(array)
        self.assertEqual([1, 2, 3, 4, 5], array)

    def test_quick_sort_random(self):
        array = list(range(1000))
        shuffle(array)
        quick_sort(array)
        self.assertEqual(list(range(1000)), array)
