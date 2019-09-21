from IntroductionToAlgorithm3E.Chapter33.convex_hull import find_convex_hull
from Test.unit_test_template import UnitTestTemplate


class ConvexHullTest(UnitTestTemplate):
    def test_find_convex_hull(self):
        points = [[0, 3], [2, 2], [1, 1], [2, 1],
                  [3, 0], [0, 0], [3, 3]]
        actual_ch = list(find_convex_hull(points))
        expected_ch = list([[0, 0], [3, 0], [3, 3], [0, 3]])
        self.assertEquals(expected_ch, actual_ch)
