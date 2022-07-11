"""
https://www.hackerrank.com/challenges/the-grid-search/problem

Given a 2D array of digits or grid, try to find the occurrence of a another 2D pattern of digits within the grid
"""
from regex import finditer


def does_pattern_exist(grid, pattern):
    return does_pattern_exist_regex(grid, pattern)


def does_pattern_exist_naive(grid, pattern):
    grid_index = 0
    pattern_index = 0
    start_position = -1

    while grid_index < len(grid) and pattern_index < len(pattern):
        first_index = grid[grid_index].find(pattern[pattern_index], start_position if start_position > -1 else 0, len(grid[grid_index]))

        if first_index >= 0:
            pattern_index += 1

            if start_position == -1:
                start_position = first_index
        elif start_position != -1:
            break

        grid_index += 1

    found = (pattern_index == len(pattern))

    return found


def does_pattern_exist_regex(grid, pattern):
    grid_index = 0
    pattern_index = 0
    start_positions = []

    while grid_index < len(grid) and pattern_index < len(pattern):
        occurrences = [m.start() for m in finditer(pattern[pattern_index], grid[grid_index], overlapped=True)]

        if len(occurrences) > 0:
            if pattern_index == 0:
                start_positions = occurrences
                pattern_index += 1
            else:
                start_positions = [x for x in start_positions if x in occurrences]
                if len(start_positions) > 0:
                    pattern_index += 1
                else:
                    break

        elif len(start_positions) > 0:
            break

        grid_index += 1

    return pattern_index == len(pattern)
