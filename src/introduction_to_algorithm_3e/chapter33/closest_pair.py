"""
Find closest pair of points in O(nlogn) time
"""
import operator

from introduction_to_algorithm_3e.chapter33.euclidean_geometry import is_same_point, find_distance_between_2_points


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
    p = points.copy()
    x = sorted(points.copy(), key=operator.itemgetter(0))
    y = sorted(points.copy(), key=operator.itemgetter(1))
    return _find_closest_pair_fast_helper(p, x, y)


def _find_closest_pair_fast_helper(points, x, y):
    if len(points) <= 3:
        return find_closest_pair_brute_force(points)
    else:
        # divide
        x_coordinates = [point[0] for point in x]
        median_x_division = x_coordinates[len(x) // 2]

        left_points = []
        right_points = []
        left_points_by_x = []
        right_points_by_x = []
        left_points_by_y = []
        right_points_by_y = []

        for point in points:
            if point[0] < median_x_division:
                left_points += [point]
            else:
                right_points += [point]

        for point in x:
            if point in left_points:
                left_points_by_x += [point]
            else:
                right_points_by_x += [point]

        for point in y:
            if point in left_points:
                left_points_by_y += [point]
            else:
                right_points_by_y += [point]

        # conquer
        min_left_point_a, min_left_point_b, min_left_distance = \
            _find_closest_pair_fast_helper(left_points, left_points_by_x, left_points_by_y)
        min_right_point_a, min_right_point_b, min_right_distance = \
            _find_closest_pair_fast_helper(right_points, right_points_by_x, right_points_by_y)

        if min_left_distance < min_right_distance:
            min_point_a = min_left_point_a
            min_point_b = min_left_point_b
            min_distance = min_left_distance
        else:
            min_point_a = min_right_point_a
            min_point_b = min_right_point_b
            min_distance = min_right_distance

        # combine
        y_prime = []
        for point in y:
            if median_x_division - min_distance <= point[0] <= median_x_division + min_distance:
                y_prime += [point]

        min_strip_distance = float('inf')
        min_strip_point_a = None
        min_strip_point_b = None

        for i in range(len(y_prime)):
            next_range = i + 7 if (i + 7) < len(y_prime) else len(y_prime) - i - 1
            for j in range(i + 1, next_range):
                d = find_distance_between_2_points(y_prime[i], y_prime[j])

                if d < min_strip_distance:
                    min_strip_point_a = y_prime[i]
                    min_strip_point_b = y_prime[j]
                    min_strip_distance = d

        if min_strip_distance < min_distance:
            min_point_a = min_strip_point_a
            min_point_b = min_strip_point_b
            min_distance = min_strip_distance

        return min_point_a, min_point_b, min_distance
