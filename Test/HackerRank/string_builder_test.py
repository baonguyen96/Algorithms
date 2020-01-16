from HackerRank.string_builder import build_string
from Test.unit_test_template import UnitTestTemplate


class StringBuilderTest(UnitTestTemplate):
    def test_build_string_insert_only(self):
        target_sting = 'abc'
        cost_to_create = 2
        cost_to_copy = 1
        expected = 6
        actual = build_string(target_sting, cost_to_create, cost_to_copy)
        self.assertEqual(expected, actual)

    def test_build_string_all_repeat(self):
        target_sting = 'aaaa'
        cost_to_create = 2
        cost_to_copy = 1
        expected = 4
        actual = build_string(target_sting, cost_to_create, cost_to_copy)
        self.assertEqual(expected, actual)

    def test_build_string_a(self):
        target_sting = 'aabaacaba'
        cost_to_create = 4
        cost_to_copy = 5
        expected = 26
        actual = build_string(target_sting, cost_to_create, cost_to_copy)
        self.assertEqual(expected, actual)

    def test_build_string_b(self):
        target_sting = 'bacbacacb'
        cost_to_create = 8
        cost_to_copy = 9
        expected = 42
        actual = build_string(target_sting, cost_to_create, cost_to_copy)
        self.assertEqual(expected, actual)
