import math


def find_distance_between_2_points(p0, p1):
    distance = math.sqrt((p1[0] - p0[0]) ** 2 + (p1[1] - p0[1]) ** 2)
    return distance


def find_angle_counter_clockwise(p0, p1, p2):
    angle = math.degrees(math.atan2(p2[1] - p1[1], p2[0] - p1[0]) -
                         math.atan2(p0[1] - p1[1], p0[0] - p1[0]))

    if angle == 360:
        angle = 0
    elif angle < 0:
        angle = angle + 360
    else:
        angle = angle

    return angle


def is_same_point(point_a, point_b):
    return point_a[0] == point_b[0] and point_a[1] == point_b[1]
