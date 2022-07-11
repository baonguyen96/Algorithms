from src.interviewing_io.missing_number import get_missing_number
from tests.unit_test_template import UnitTestTemplate


class MissingNumberTest(UnitTestTemplate):
    def test_get_missing_number(self):
        arr1 = [1, 2, 3]
        arr2 = [3, 1]
        expected = 2
        actual = get_missing_number(arr1, arr2)
        self.assertEqual(expected, actual)

    def test_get_missing_number_long(self):
        arr1 = list(range(0, 1000001))
        arr2 = list(range(0, 1000000))
        expected = 1000000
        actual = get_missing_number(arr1, arr2)
        self.assertEqual(expected, actual)
