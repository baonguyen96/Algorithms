import math

from IntroductionToAlgorithm3E.Chapter33.convex_hull import find_angle_counter_clockwise, \
    find_distance_between_2_points, find_convex_hull
from Test.unit_test_template import UnitTestTemplate


class ConvexHullTest(UnitTestTemplate):
    def test_find_angle_counter_clockwise_lines(self):
        angle = find_angle_counter_clockwise([1, 0], [0, 0], [1, 0])
        self.assertEquals(0, angle)

        angle = find_angle_counter_clockwise([1, 0], [0, 0], [-1, 0])
        self.assertEquals(180, angle)

    def test_find_angle_counter_clockwise_square(self):
        angle = find_angle_counter_clockwise([-1, 0], [0, 0], [0, 1])
        self.assertEquals(270, angle)

        angle = find_angle_counter_clockwise([-1, 0], [0, 0], [0, -1])
        self.assertEquals(90, angle)

    def test_find_angle_counter_clockwise_45(self):
        angle = find_angle_counter_clockwise([-1, 0], [0, 0], [-1, 1])
        self.assertEquals(315, angle)

        angle = find_angle_counter_clockwise([1, 0], [0, 0], [1, 1])
        self.assertEquals(45, angle)

    def test_find_distance_between_2_points_line(self):
        distance = find_distance_between_2_points([0, 0], [1, 0])
        self.assertEquals(1, distance)

        distance = find_distance_between_2_points([-1, 0], [1, 0])
        self.assertEquals(2, distance)

    def test_find_distance_between_2_points_angle(self):
        distance = find_distance_between_2_points([0, 0], [0, 0])
        self.assertEquals(math.sqrt(0), distance)

        distance = find_distance_between_2_points([1, 0], [0, 0])
        self.assertEquals(math.sqrt(1), distance)

        distance = find_distance_between_2_points([1, 1], [0, 0])
        self.assertEquals(math.sqrt(2), distance)

    def test_find_convex_hull(self):
        points = [[0, 3], [2, 2], [1, 1], [2, 1],
                  [3, 0], [0, 0], [3, 3]]
        actual_ch = list(find_convex_hull(points))
        expected_ch = list([[0, 0], [3, 0], [3, 3], [0, 3]])
        self.assertEquals(expected_ch, actual_ch)
