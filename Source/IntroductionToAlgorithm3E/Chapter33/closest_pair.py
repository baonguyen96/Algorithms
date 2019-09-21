"""
Find closest pair of points in O(nlogn) time
"""
import operator

from IntroductionToAlgorithm3E.Chapter33.euclidean_geometry import is_same_point, find_distance_between_2_points


def find_closest_pair_brute_force(points):
    min_distance = float("inf")
    min_point_a = None
    min_point_b = None

    for point_a in points:
        for point_b in points:
            if is_same_point(point_a, point_b):
                continue

            distance = find_distance_between_2_points(point_a, point_b)

            if distance < min_distance:
                min_distance = distance
                min_point_a = point_a
                min_point_b = point_b

    return min_point_a, min_point_b, min_distance


def find_closest_pair_fast(points):
    points = sorted(points, key=operator.itemgetter(0, 1))
