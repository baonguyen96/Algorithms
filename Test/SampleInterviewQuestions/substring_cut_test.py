from SampleInterviewQuestions.substring_cut import get_max_substring_cut
from Test.unit_test_template import UnitTestTemplate


class SubStringCut(UnitTestTemplate):
    def test_get_max_substring_cut(self):
        string = 'abcdedeara'
        expected = 3
        actual = get_max_substring_cut(string)
        self.assertEqual(expected, actual)

    def test_get_max_substring_cut_palindrome(self):
        string = 'aabbbbaa'
        expected = 4
        actual = get_max_substring_cut(string)
        self.assertEqual(expected, actual)

    def test_get_max_substring_empty(self):
        string = ''
        expected = 0
        actual = get_max_substring_cut(string)
        self.assertEqual(expected, actual)

    def test_get_max_substring_all_unique(self):
        string = 'abcde'
        expected = 0
        actual = get_max_substring_cut(string)
        self.assertEqual(expected, actual)

    def test_get_max_substring_random(self):
        string = 'zzzxxxzzz'
        expected = 4
        actual = get_max_substring_cut(string)
        self.assertEqual(expected, actual)
