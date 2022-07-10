"""
Problem 16.1-5

Consider a modification to the activity-selection problem in which each activity ai has,
    in addition to a start and finish time, a value vi .
    The objective is no longer to maximize the number of activities scheduled,
    but instead to maximize the total value of the activities scheduled.
    That is, we wish to choose a set A of compatible activities such that sum of the values
    is maximized. Give a polynomial-time algorithm for this problem.
"""


def get_compatible_activities_max_values(activities):
    for mid in activities:
        for start in activities:
            for end in activities:
                pass
