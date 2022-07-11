"""
https://www.hackerrank.com/challenges/counting-valleys/problem

Gary is an avid hiker. He tracks his hikes meticulously, paying close attention to small details like topography.
    During his last hike he took exactly  steps. For every step he took, he noted if it was an uphill U, or a downhill D step.
    Gary's hikes start and end at sea level and each step up or down represents a  unit change in altitude.
    We define the following terms:
        - A mountain is a sequence of consecutive steps above sea level,
        starting with a step up from sea level and ending with a step down to sea level.
        - A valley is a sequence of consecutive steps below sea level,
        starting with a step down from sea level and ending with a step up to sea level.
    Given Gary's sequence of up and down steps during his last hike, find and print the number of valleys he walked through.

e.g.
For example, if Gary's path is [DDUUUUDD], he first enters a valley 2 units deep.
    Then he climbs out an up onto a mountain 4 units high.
    Finally, he returns to sea level and ends his hike.
    Totally, 1 valley.
"""


def count_valley(path):
    current_level = 0
    path = path.upper()
    count = 0

    for direction in path:
        if direction == 'U':
            current_level += 1
        else:
            current_level -= 1

        if current_level == 0 and direction == 'U':
            count += 1

    return count
