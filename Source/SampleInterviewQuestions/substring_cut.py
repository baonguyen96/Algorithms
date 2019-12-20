"""
Given a string, divide into 2 substrings s.t. the substrings have the most possible characters in common.

E.g.
    'abcdecdefg' -> 'abcde' & 'cdefg' = 3
    'aabbbbaa' -> 'aabb' & 'bbaa' = 4
"""


def get_max_substring_cut(string):
    max_cut = 0

    for i in range(1, len(string) - 1):
        left = string[:i]
        right = string[i:]

        left_count = get_character_count(left)
        right_count = get_character_count(right)

        current_cut = 0

        for c in left_count:
            if c in right_count.keys():
                current_cut += min(left_count[c], right_count[c])

        if current_cut > max_cut:
            max_cut = current_cut

    return max_cut


def get_character_count(string):
    count = {}

    for c in string:
        if c in count.keys():
            count[c] += 1
        else:
            count[c] = 1

    return count
