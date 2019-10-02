"""
Problem 15-2

Give an efficient algorithm to find the longest palindrome
    that is a subsequence of a given input string.
    For example, given the input character, the algorithm
should return carac.
"""
import copy

from IntroductionToAlgorithm3E.Chapter15.longest_common_subsequence import find_longest_common_subsequence


def find_longest_palindrome(string):
    forward_string = list(copy.deepcopy(string))
    backward_string = list(string[::-1])
    longest_palindrome = find_longest_common_subsequence(forward_string, backward_string)
    return ''.join(longest_palindrome)
