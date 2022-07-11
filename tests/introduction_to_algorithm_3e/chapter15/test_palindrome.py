import src.introduction_to_algorithm_3e.chapter15.palindrome as p
from tests.unit_test_template import UnitTestTemplate


class PalindromeTest(UnitTestTemplate):
    def test_find_longest_palindrome_single_character(self):
        s = 'a'
        lp = p.find_longest_palindrome(s)
        self.assertEqual('a', lp)

    def test_find_longest_palindrome_full_word(self):
        s = 'aibohphobia'
        lp = p.find_longest_palindrome(s)
        self.assertEqual('aibohphobia', lp)

        s = 'racecar'
        lp = p.find_longest_palindrome(s)
        self.assertEqual('racecar', lp)

    def test_find_longest_palindrome_partial(self):
        s = 'character'
        lp = p.find_longest_palindrome(s)
        self.assertEqual('carac', lp)
