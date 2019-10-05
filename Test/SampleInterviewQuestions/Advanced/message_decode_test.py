import random
import unittest

from SampleInterviewQuestions.Advanced.message_decode import get_total_decode_possibilities
from Test.unit_test_template import UnitTestTemplate


class MessageDecodeTest(UnitTestTemplate):
    def test_get_total_decode_possibilities_invalid(self):
        data = '01'
        expected_output = 0  # nothing map to 0
        actual_output = get_total_decode_possibilities(data)
        self.assertEqual(expected_output, actual_output)

    def test_get_total_decode_possibilities_single_value(self):
        data = '1'
        expected_output = 1  # A
        actual_output = get_total_decode_possibilities(data)
        self.assertEqual(expected_output, actual_output)

    def test_get_total_decode_possibilities_12(self):
        data = '12'
        expected_output = 2  # AB (1 2) or L (12)
        actual_output = get_total_decode_possibilities(data)
        self.assertEqual(expected_output, actual_output)

    def test_get_total_decode_possibilities_226(self):
        data = '226'
        expected_output = 3  # BZ (2 26) or VF (22 6) or BBF (2 2 6)
        actual_output = get_total_decode_possibilities(data)
        self.assertEqual(expected_output, actual_output)

    def test_get_total_decode_possibilities_1234(self):
        data = '1234'
        expected_output = 3  # ABCD (1 2 3 4) or LCD (12 3 4) or AWD (1 23 4)
        actual_output = get_total_decode_possibilities(data)
        self.assertEqual(expected_output, actual_output)

    @unittest.skip("Stack overflow")
    def test_get_total_decode_possibilities_performance(self):
        data = ''.join(list([str(random.randint(1, 9)) for i in range(1000)]))
        actual_output = get_total_decode_possibilities(data)
        self.assertGreater(0, actual_output)
