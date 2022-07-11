"""
Find longest consecutive characters in a string
Return that charactter with its longest consecutive count
"""


def get_longest_consecutive_character(string):
    if string is None or len(string) == 0:
        return None

    consecutive_char_count = {string[0]: 1}
    local_consecutive_count = 1

    for i in range(1, len(string)):
        if string[i] == string[i - 1]:
            local_consecutive_count += 1
            consecutive_char_count[string[i]] = local_consecutive_count
        else:
            local_consecutive_count = 1

            if string[i] not in consecutive_char_count:
                consecutive_char_count[string[i]] = local_consecutive_count

    current_max_count = -1
    current_max_char = None

    for key, value in consecutive_char_count.items():
        if value > current_max_count:
            current_max_char = key
            current_max_count = value

    return {current_max_char: current_max_count}
