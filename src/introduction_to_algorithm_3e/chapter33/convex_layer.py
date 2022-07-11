"""
Problem 33-1

Given a set Q of points in the plane, we define the Convex layers of Q inductively.
    The first convex layer ofQconsists of those points inQthat are vertices of CH(Q).
    For i > 1, define Qi to consist of the points of Q with all points in convex layers 1, 2, ..., i - 1 removed.
    Then, the i th convex layer of Q is CH(Qi) if Qi is not empty and
is undefined otherwise.
"""
import copy

from src.introduction_to_algorithm_3e.chapter33.convex_hull import find_convex_hull


def find_convex_layers(points):
    convex_layers = []
    temp_points = copy.deepcopy(points)

    while len(temp_points) > 0:
        ch = find_convex_hull(temp_points)
        convex_layers += [ch]
        temp_points = [p for p in temp_points if p not in ch]

    return convex_layers
