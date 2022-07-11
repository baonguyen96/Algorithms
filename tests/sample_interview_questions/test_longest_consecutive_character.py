from src.sample_interview_questions.longest_consecutive_character import get_longest_consecutive_character
from tests.unit_test_template import UnitTestTemplate


class LongestConsecutiveCharacterTest(UnitTestTemplate):
    def test_get_longest_consecutive_character_empty(self):
        string = ''
        expected = None
        actual = get_longest_consecutive_character(string)
        self.assertEqual(expected, actual)

        string = None
        expected = None
        actual = get_longest_consecutive_character(string)
        self.assertEqual(expected, actual)

    def test_get_longest_consecutive_character_single(self):
        string = 'abcde'
        expected = {'a': 1}
        actual = get_longest_consecutive_character(string)
        self.assertEqual(expected, actual)

    def test_get_longest_consecutive_character(self):
        string = 'aabcddbbbea'
        expected = {'b': 3}
        actual = get_longest_consecutive_character(string)
        self.assertEqual(expected, actual)
