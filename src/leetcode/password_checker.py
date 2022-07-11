"""
https://leetcode.com/problems/strong-password-checker/
"""


def is_strong_password(password):
    if len(password) < 6 or len(password) > 20:
        return False

    has_lowercase = False
    has_uppercase = False
    has_digit = False
    consecutive_char_count = 0
    last_char = password[0]

    for c in password:
        if c.isupper():
            has_uppercase = True

        if c.islower():
            has_lowercase = True

        if c.isdigit():
            has_digit = True

        if last_char == c:
            consecutive_char_count += 1
        else:
            consecutive_char_count = 1

        if consecutive_char_count >= 3:
            break

        last_char = c

    return has_lowercase and has_uppercase and has_digit and consecutive_char_count < 3
