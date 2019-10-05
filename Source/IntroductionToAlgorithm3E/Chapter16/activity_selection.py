"""
Suppose we have a set S{a1, a2, ... an} of n proposed activities
    that wish to use a resource which can serve only one activity at a time.
    Each activity ai has a start time si and a finish time fi, where 0 <= si < fi < inf.
    If selected, activity ai takes place during the half-open time interval [si, fi).
    Activities ai and aj are compatible if the intervals [si, fi) and [sj, fj) do not overlap.
    In the activity-selection problem, we wish to select a maximum-size subset of
    mutually compatible activities.
"""


def get_max_activities_select_first_to_finish(activities):
    """
    Assume that the activities are sorted in monotonically increasing order of finish time.
    Or can just sort, which makes this O(nlgn) time. Otherwise, O(n) time.
    """
    activity_name = 0
    activity_start = 1
    activity_finish = 2

    target_activities = []
    target_activities += [activities[0]]

    for i in range(1, len(activities)):
        previous_activity = target_activities[-1]

        if activities[i][activity_start] <= previous_activity[activity_finish]:
            continue

        target_activities += [activities[i]]

    return [activity[activity_name] for activity in target_activities]


def get_max_activities_select_last_to_start(activities):
    """
    Assume that the activities are sorted in monotonically increasing order of start time.
    Or can just sort, which makes this O(nlgn) time. Otherwise, O(n) time.
    """
    activity_name = 0
    activity_start = 1
    activity_finish = 2

    target_activities = []
    target_activities += [activities[-1]]

    for i in range(len(activities) - 2, -1, -1):
        previous_activity = target_activities[-1]

        if activities[i][activity_finish] >= previous_activity[activity_start]:
            continue

        target_activities += [activities[i]]

    target_activities.reverse()
    return [activity[activity_name] for activity in target_activities]
