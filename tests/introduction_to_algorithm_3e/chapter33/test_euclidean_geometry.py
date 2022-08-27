import math

from src.introduction_to_algorithm_3e.chapter33.euclidean_geometry \
    import find_angle_counter_clockwise, find_distance_between_2_points, is_same_point
from tests.unit_test_template import UnitTestTemplate


class EuclideanGeometryTest(UnitTestTemplate):
    def test_find_angle_counter_clockwise_lines(self):
        angle = find_angle_counter_clockwise([1, 0], [0, 0], [1, 0])
        self.assertEqual(0, angle)

        angle = find_angle_counter_clockwise([1, 0], [0, 0], [-1, 0])
        self.assertEqual(180, angle)

    def test_find_angle_counter_clockwise_square(self):
        angle = find_angle_counter_clockwise([-1, 0], [0, 0], [0, 1])
        self.assertEqual(270, angle)

        angle = find_angle_counter_clockwise([-1, 0], [0, 0], [0, -1])
        self.assertEqual(90, angle)

    def test_find_angle_counter_clockwise_45(self):
        angle = find_angle_counter_clockwise([-1, 0], [0, 0], [-1, 1])
        self.assertEqual(315, angle)

        angle = find_angle_counter_clockwise([1, 0], [0, 0], [1, 1])
        self.assertEqual(45, angle)

    def test_find_distance_between_2_points_line(self):
        distance = find_distance_between_2_points([0, 0], [1, 0])
        self.assertEqual(1, distance)

        distance = find_distance_between_2_points([-1, 0], [1, 0])
        self.assertEqual(2, distance)

    def test_find_distance_between_2_points_angle(self):
        distance = find_distance_between_2_points([0, 0], [0, 0])
        self.assertEqual(math.sqrt(0), distance)

        distance = find_distance_between_2_points([1, 0], [0, 0])
        self.assertEqual(math.sqrt(1), distance)

        distance = find_distance_between_2_points([1, 1], [0, 0])
        self.assertEqual(math.sqrt(2), distance)

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
