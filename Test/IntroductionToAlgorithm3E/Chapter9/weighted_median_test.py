import IntroductionToAlgorithm3E.Chapter9.weighted_median as wm
from Test.unit_test_template import UnitTestTemplate
from statistics import median as med


class WeightedMedianTest(UnitTestTemplate):
    def test_get_median_using_sort(self):
        array = [1, 1, 1, 1, 1, 1, 1, 11, 5]
        median = wm.get_median_using_sort(array)
        self.assertEqual(med(array), median)

        array = [0.1, 0.35, 0.05, 0.1, 0.15, 0.05, 0.2]
        median = wm.get_median_using_sort(array)
        self.assertEqual(med(array), median)

        array = [1, 2, 2, 3, 3, 3]
        median = wm.get_median_using_sort(array)
        self.assertEqual(2, median)

    def test_get_median_using_select(self):
        array = [1, 1, 1, 1, 1, 1, 1, 11, 5]
        median = wm.get_median_using_select(array)
        self.assertEqual(med(array), median)

        array = [0.1, 0.35, 0.05, 0.1, 0.15, 0.05, 0.2]
        median = wm.get_median_using_select(array)
        self.assertEqual(med(array), median)

        array = [1, 2, 2, 3, 3, 3]
        median = wm.get_median_using_select(array)
        self.assertEqual(2, median)

    def test_get_weighted_median_using_sort_positive(self):
        array = [
            [0.1, 0.1],
            [0.35, 0.35],
            [0.05, 0.05],
            [0.1, 0.1],
            [0.15, 0.15],
            [0.05, 0.05],
            [0.2, 0.2]
        ]

        wegihted_med = wm.get_weighted_median_using_sort(array)
        self.assertEqual(0.2, wegihted_med)

        array = [
            [1, 1],
            [2, 2],
            [3, 3]
        ]

        wegihted_med = wm.get_weighted_median_using_sort(array)
        self.assertEqual(2, wegihted_med)

        array = [
            [13, 10],
            [23, 3],
            [54, 4]
        ]

        wegihted_med = wm.get_weighted_median_using_sort(array)
        self.assertEqual(13, wegihted_med)

    def test_get_weighted_median_using_select(self):
        array = [
            [0.1, 0.1],
            [0.35, 0.35],
            [0.05, 0.05],
            [0.1, 0.1],
            [0.15, 0.15],
            [0.05, 0.05],
            [0.2, 0.2]
        ]

        weighted_med = wm.get_weighted_median_using_select(array)
        self.assertEqual(0.2, weighted_med)

        array = [
            [1, 1],
            [2, 2],
            [3, 3]
        ]

        weighted_med = wm.get_weighted_median_using_select(array)
        self.assertEqual(2, weighted_med)

        array = [
            [13, 10],
            [23, 3],
            [54, 4]
        ]

        weighted_med = wm.get_weighted_median_using_select(array)
        self.assertEqual(13, weighted_med)
