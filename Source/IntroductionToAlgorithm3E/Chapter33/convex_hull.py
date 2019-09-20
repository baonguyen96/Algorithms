"""
Problem 33.3-6

Show how to implement the incremental method for computing the convex hull
    of n points so that it runs in O(nlgn) time (Graham's Scan)
"""
import math
import operator


def find_convex_hull(points):
    points = sorted(points, key=operator.itemgetter(1, 0))
    p0 = points[0]
    remaining_points = sort_points_by_polar_angle_from_origin(p0, points[1:])

    p1 = remaining_points[0]
    p2 = remaining_points[1]
    s = [p0, p1, p2]

    for i in range(2, len(remaining_points)):
        top = s[len(s) - 1]
        next_to_top = s[len(s) - 2]
        point_i = remaining_points[i]
        while find_angle_counter_clockwise(top, next_to_top, point_i) > 180:
            s.pop()
            top = s[len(s) - 1]
            next_to_top = s[len(s) - 2]
        s.append(point_i)
    return s


def sort_points_by_polar_angle_from_origin(origin, points):
    point_angles = {}

    x_axis = [origin[0] + 1, origin[1]]

    for point in points:
        angle = find_angle_counter_clockwise(x_axis, origin, point)

        if angle in point_angles:
            existed_point = point_angles[angle]
            current_distance = find_distance_between_2_points(origin, existed_point)
            new_distance = find_distance_between_2_points(origin, point)

            if new_distance > current_distance:
                point_angles[angle] = point
        else:
            point_angles[angle] = point

    sorted_points = []

    for angle in sorted(point_angles):
        sorted_points += [point_angles[angle]]

    return sorted_points


def find_distance_between_2_points(p0, p1):
    distance = math.sqrt((p1[0] - p0[0]) ** 2 + (p1[1] - p0[1]) ** 2)
    return distance


def find_angle_counter_clockwise(p0, p1, p2):
    angle = math.degrees(math.atan2(p2[1] - p1[1], p2[0] - p1[0]) - \
                         math.atan2(p0[1] - p1[1], p0[0] - p1[0]))

    if angle == 360:
        angle = 0
    elif angle < 0:
        angle = angle + 360
    else:
        angle = angle

    return angle
