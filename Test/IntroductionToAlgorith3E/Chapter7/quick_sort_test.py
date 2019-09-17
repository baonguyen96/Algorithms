from random import shuffle

from IntroductionToAlgorithm3E.Chapter7.quick_sort import quick_sort
from Test.unit_test_template import UnitTestTemplate


class QuickSortTest(UnitTestTemplate):
    def test_quick_sort(self):
        array = list(range(10))
        shuffle(array)
        quick_sort(array)
        self.assertEqual(list(range(10)), array)
