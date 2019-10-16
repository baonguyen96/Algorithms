import math
import random

from SampleInterviewQuestions.string_permutation import get_all_permutation
from Test.unit_test_template import UnitTestTemplate


class StringPermutationTest(UnitTestTemplate):
    def test_get_all_permutation_empty(self):
        s = None
        self.assertEqual(None, get_all_permutation(s))

    def test_get_all_permutation_single(self):
        s = 'a'
        self.assertEqual(['a'], get_all_permutation(s))

    def test_get_all_permutation_2_chars(self):
        s = 'ab'
        expected = ['ab', 'ba']
        actual = get_all_permutation(s)
        self.assertEqual(expected, actual)

    def test_get_all_permutation_3_chars(self):
        s = 'abc'
        expected = ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
        actual = get_all_permutation(s)
        self.assertEqual(set(expected), set(actual))

    def test_get_all_permutation_performance(self):
        length = 8
        s = ''.join([chr(random.randint(41, 41 + 26)) for c in range(length)])
        expected = math.factorial(length)
        actual = len(get_all_permutation(s))
        self.assertEqual(expected, actual)
