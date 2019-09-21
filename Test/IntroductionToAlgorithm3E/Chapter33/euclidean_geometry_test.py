import math

from IntroductionToAlgorithm3E.Chapter33.euclidean_geometry \
    import find_angle_counter_clockwise, find_distance_between_2_points, is_same_point
from Test.unit_test_template import UnitTestTemplate


class EuclideanGeometryTest(UnitTestTemplate):
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

    def test_is_same_point_true(self):
        point_a = [0, 0]
        point_b = [0, 0]
        self.assertTrue(is_same_point(point_a, point_b))

    def test_is_same_point_different_x(self):
        point_a = [0, 0]
        point_b = [-1, 0]
        self.assertFalse(is_same_point(point_a, point_b))

    def test_is_same_point_different_y(self):
        point_a = [0, 0]
        point_b = [0, 1]
        self.assertFalse(is_same_point(point_a, point_b))
