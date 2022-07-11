from src.hacker_rank.append_delete import is_transformation_possible
from tests.unit_test_template import UnitTestTemplate


class AppendDeleteTest(UnitTestTemplate):
    def test_is_transformation_possible_true(self):
        source = 'hackerhappy'
        destination = 'hackerrank'
        steps = 9
        expected = True
        actual = is_transformation_possible(source, destination, steps)
        self.assertEqual(expected, actual)

    def test_is_transformation_possible_true_already_equal(self):
        source = 'abc'
        destination = 'abc'
        steps = 7
        expected = True
        actual = is_transformation_possible(source, destination, steps)
        self.assertEqual(expected, actual)

    def test_is_transformation_possible_false(self):
        source = 'ashley'
        destination = 'ash'
        steps = 2
        expected = False
        actual = is_transformation_possible(source, destination, steps)
        self.assertEqual(expected, actual)

    def test_is_transformation_possible_false_empty(self):
        source = ''
        destination = 'destination'
        steps = 2
        expected = False
        actual = is_transformation_possible(source, destination, steps)
        self.assertEqual(expected, actual)

        source = 'source'
        destination = ''
        steps = 2
        expected = False
        actual = is_transformation_possible(source, destination, steps)
        self.assertEqual(expected, actual)

    def test_is_transformation_possible_true_empty(self):
        source = ''
        destination = 'destination'
        steps = len(destination)
        expected = True
        actual = is_transformation_possible(source, destination, steps)
        self.assertEqual(expected, actual)

        source = 'source'
        destination = ''
        steps = len(source)
        expected = True
        actual = is_transformation_possible(source, destination, steps)
        self.assertEqual(expected, actual)
