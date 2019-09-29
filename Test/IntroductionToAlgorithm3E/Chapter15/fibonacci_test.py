from IntroductionToAlgorithm3E.Chapter15 import fibonacci as fib
from Test.unit_test_template import UnitTestTemplate


class FibonacciTest(UnitTestTemplate):
    def test_fibonacci_recursive(self):
        self.assertEqual(1, fib.fibonacci_recursive(0))
        self.assertEqual(3, fib.fibonacci_recursive(3))
        self.assertEqual(8, fib.fibonacci_recursive(5))

    def test_fibonacci_loop(self):
        self.assertEqual(1, fib.fibonacci_loop(0))
        self.assertEqual(3, fib.fibonacci_loop(3))
        self.assertEqual(8, fib.fibonacci_loop(5))
