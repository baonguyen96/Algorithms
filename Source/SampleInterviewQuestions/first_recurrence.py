"""
Find the first repeated character in a string
"""


def get_first_recurrence(string):
    seen = set()

    for c in string:
        if c in seen:
            return c

        seen.add(c)

    return None
