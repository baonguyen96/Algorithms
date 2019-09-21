from IntroductionToAlgorithm3E.Chapter9.weighted_median import get_median, get_weighted_median
from Test.unit_test_template import UnitTestTemplate
from statistics import median as med


class WeightedMedianTest(UnitTestTemplate):
    def test_get_median(self):
        array = [1, 1, 1, 1, 1, 1, 1, 11, 5]
        median = get_median(array)
        self.assertEqual(med(array), median)

        array = [0.1, 0.35, 0.05, 0.1, 0.15, 0.05, 0.2]
        median = get_median(array)
        self.assertEqual(med(array), median)

        array = list(range(9))
        median = get_median(array)
        self.assertEqual(med(array), median)

        array = list(range(10))
        median = get_median(array)
        self.assertEqual(med(array), median)

    def test_get_weighted_median(self):
        array = [
            [0.1, 0.1],
            [0.35, 0.35],
            [0.05, 0.05],
            [0.1, 0.1],
            [0.15, 0.15],
            [0.05, 0.05],
            [0.2, 0.2]
        ]

        wm = get_weighted_median(array)
        self.assertEqual(0.2, wm)

        array = [
            [1, 1],
            [2, 2],
            [3, 3]
        ]

        wm = get_weighted_median(array)
        self.assertEqual(2, wm)

        array = [
            [13, 10],
            [23, 3],
            [54, 4]
        ]

        wm = get_weighted_median(array)
        self.assertEqual(13, wm)
