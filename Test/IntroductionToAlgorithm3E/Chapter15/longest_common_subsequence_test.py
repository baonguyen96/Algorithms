import copy
import random

import IntroductionToAlgorithm3E.Chapter15.longest_common_subsequence as lcs
from Test.unit_test_template import UnitTestTemplate


class LongestCommonSubsequenceTest(UnitTestTemplate):
    def test_reconstruct_longest_common_subsequence(self):
        x = list('ABCBDAB')
        y = list('BDCABA')
        table = [[0, 0, 0, 1, 1, 1],
                 [1, 1, 1, 1, 2, 2],
                 [1, 1, 2, 2, 2, 2],
                 [1, 1, 2, 2, 3, 3],
                 [1, 2, 2, 2, 3, 3],
                 [1, 2, 2, 3, 3, 4],
                 [1, 2, 2, 3, 4, 4]]
        expected_sequence = list('BCBA')
        actual_sequence = lcs.reconstruct_longest_common_subsequence(x, y, table)
        self.assertEqual(expected_sequence, actual_sequence)

    def test_find_longest_common_subsequence_empty(self):
        x = list('A')
        y = list('B')
        expected_lcs = []
        actual_lcs = lcs.find_longest_common_subsequence(x, y)
        self.assertEqual(expected_lcs, actual_lcs)

        x = list('')
        y = list('')
        expected_lcs = []
        actual_lcs = lcs.find_longest_common_subsequence(x, y)
        self.assertEqual(expected_lcs, actual_lcs)

    def test_find_longest_common_subsequence_single(self):
        x = list('A')
        y = list('A')
        expected_lcs = ['A']
        actual_lcs = lcs.find_longest_common_subsequence(x, y)
        self.assertEqual(expected_lcs, actual_lcs)

    def test_find_longest_common_subsequence_multiple(self):
        x = list('ABCBDAB')
        y = list('BDCABA')
        expected_lcs = list('BCBA')
        actual_lcs = lcs.find_longest_common_subsequence(x, y)
        self.assertEqual(expected_lcs, actual_lcs)

    def test_find_longest_common_subsequence_multiple_int(self):
        x = [7, 8, 9]
        y = [8, 9, 10, 11, 12]
        expected_lcs = [8, 9]
        actual_lcs = lcs.find_longest_common_subsequence(x, y)
        self.assertEqual(expected_lcs, actual_lcs)

    def test_find_longest_common_subsequence_performance(self):
        x = [random.randint(0, 100) for i in range(1000)]
        y = [random.randint(200, 1000) for i in range(1000)] + x + \
            [random.randint(200, 300) for i in range(2000)]
        expected_lcs = copy.deepcopy(x)
        actual_lcs = lcs.find_longest_common_subsequence(x, y)
        self.assertEqual(expected_lcs, actual_lcs)
