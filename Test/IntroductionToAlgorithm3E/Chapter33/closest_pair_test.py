import random

from IntroductionToAlgorithm3E.Chapter33.closest_pair import find_closest_pair_brute_force, find_closest_pair_fast
from IntroductionToAlgorithm3E.Chapter33.euclidean_geometry import is_same_point
from Test.unit_test_template import UnitTestTemplate


class ClosestPairTest(UnitTestTemplate):
    def test_find_closest_pair_brute_force_small(self):
        points = [
            [0, 0], [1, 0], [3, 0],
            [0, 2], [3, 3], [-4, -5]
        ]

        expected_min_point_a = [0, 0]
        expected_min_point_b = [1, 0]
        expected_min_distance = 1
        actual_min_point_a, actual_min_point_b, actual_min_distance = find_closest_pair_brute_force(points)

        self.assertEqual(expected_min_distance, actual_min_distance)

        if is_same_point(expected_min_point_a, actual_min_point_a):
            self.assertEqual(expected_min_point_b, actual_min_point_b)
        else:
            self.assertEqual(expected_min_point_a, actual_min_point_b)
            self.assertEqual(expected_min_point_b, actual_min_point_a)

    def test_find_closest_pair_brute_force_big(self):
        points = [[0, 0], [0.5, 0]]
        points += [[random.randint(10, 100) for i in range(2)] for j in range(5000)]

        expected_min_point_a = [0, 0]
        expected_min_point_b = [0.5, 0]
        expected_min_distance = 0.5
        actual_min_point_a, actual_min_point_b, actual_min_distance = find_closest_pair_brute_force(points)

        self.assertEqual(expected_min_distance, actual_min_distance)

        if is_same_point(expected_min_point_a, actual_min_point_a):
            self.assertEqual(expected_min_point_b, actual_min_point_b)
        else:
            self.assertEqual(expected_min_point_a, actual_min_point_b)
            self.assertEqual(expected_min_point_b, actual_min_point_a)

    def test_find_closest_pair_fast_small(self):
        points = [
            [0, 0], [1, 0], [3, 0],
            [0, 2], [3, 3], [-4, -5]
        ]

        expected_min_point_a = [0, 0]
        expected_min_point_b = [1, 0]
        expected_min_distance = 1
        actual_min_point_a, actual_min_point_b, actual_min_distance = find_closest_pair_fast(points)

        self.assertEqual(expected_min_distance, actual_min_distance)

        if is_same_point(expected_min_point_a, actual_min_point_a):
            self.assertEqual(expected_min_point_b, actual_min_point_b)
        else:
            self.assertEqual(expected_min_point_a, actual_min_point_b)
            self.assertEqual(expected_min_point_b, actual_min_point_a)

    '''
    Stack overflow exception occurs when having more than 30 points,
    but otherwise works fine
    '''
    def test_find_closest_pair_fast_big(self):
        points = [[0, 0], [0.5, 0]]
        points += [[random.randint(10, 100) for i in range(2)] for j in range(1000)]

        expected_min_point_a = [0, 0]
        expected_min_point_b = [0.5, 0]
        expected_min_distance = 0.5
        actual_min_point_a, actual_min_point_b, actual_min_distance = find_closest_pair_fast(points)

        self.assertEqual(expected_min_distance, actual_min_distance)

        if is_same_point(expected_min_point_a, actual_min_point_a):
            self.assertEqual(expected_min_point_b, actual_min_point_b)
        else:
            self.assertEqual(expected_min_point_a, actual_min_point_b)
            self.assertEqual(expected_min_point_b, actual_min_point_a)
