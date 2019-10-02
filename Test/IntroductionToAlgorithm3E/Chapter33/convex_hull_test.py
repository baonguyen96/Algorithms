from IntroductionToAlgorithm3E.Chapter33.convex_hull import find_convex_hull
from Test.unit_test_template import UnitTestTemplate
from Utitilies.utility import get_random_array


class ConvexHullTest(UnitTestTemplate):
    def test_find_convex_hull_small(self):
        points = [[0, 3], [2, 2], [1, 1], [2, 1],
                  [3, 0], [0, 0], [3, 3]]
        actual_ch = list(find_convex_hull(points))
        expected_ch = list([[0, 0], [3, 0], [3, 3], [0, 3]])
        self.assertEqual(expected_ch, actual_ch)

    def test_find_convex_hull_big(self):
        points = [[0, 0], [100, 0], [100, 100], [0, 100]]
        for i in range(1000):
            points += [get_random_array(2, 20, 80)]

        actual_ch = list(find_convex_hull(points))
        expected_ch = list([[0, 0], [100, 0], [100, 100], [0, 100]])
        self.assertEqual(expected_ch, actual_ch)
