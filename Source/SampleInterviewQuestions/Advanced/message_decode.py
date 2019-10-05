"""
A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given a non-empty string containing only digits, determine the total number of ways to decode it.
"""


def get_total_decode_possibilities(data):
    if '0' in data:
        return 0

    if len(data) <= 1:
        return 1

    valid_2_chars = True if 10 <= int(data[:2]) <= 26 else False
    total = get_total_decode_possibilities(data[1:])
    if valid_2_chars:
        total += get_total_decode_possibilities(data[2:])
    return total
