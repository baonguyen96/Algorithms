from LeetCode.password_checker import is_strong_password
from Test.unit_test_template import UnitTestTemplate


class PasswordCheckerTest(UnitTestTemplate):
    def test_is_strong_password_short(self):
        password = 'hello'
        expected = False
        actual = is_strong_password(password)
        self.assertEqual(expected, actual)

    def test_is_strong_password_long(self):
        password = 'a' * 21
        expected = False
        actual = is_strong_password(password)
        self.assertEqual(expected, actual)

    def test_is_strong_password_missing_lowercase(self):
        password = 'ABCDE123'
        expected = False
        actual = is_strong_password(password)
        self.assertEqual(expected, actual)

    def test_is_strong_password_missing_uppercase(self):
        password = 'abcde123'
        expected = False
        actual = is_strong_password(password)
        self.assertEqual(expected, actual)

    def test_is_strong_password_missing_digit(self):
        password = 'qwertyuiopASD'
        expected = False
        actual = is_strong_password(password)
        self.assertEqual(expected, actual)

    def test_is_strong_password_repeated(self):
        password = 'AAAbcd123'
        expected = False
        actual = is_strong_password(password)
        self.assertEqual(expected, actual)

    def test_is_strong_password_valid(self):
        password = 'Abcd123'
        expected = True
        actual = is_strong_password(password)
        self.assertEqual(expected, actual)
