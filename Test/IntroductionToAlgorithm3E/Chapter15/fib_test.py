from IntroductionToAlgorithm3E.Chapter15 import fib
from Test.unit_test_template import UnitTestTemplate

# 0 1 2 3 4 5
# 1 1 2 3 5 8


class FibonacciTest(UnitTestTemplate):
    def test_fib_recursive(self):
        self.assertEqual(1, fib.fib_recursive(0))
        self.assertEqual(3, fib.fib_recursive(3))
        self.assertEqual(8, fib.fib_recursive(5))

    def test_fib_loop(self):
        self.assertEqual(1, fib.fib_loop(0))
        self.assertEqual(3, fib.fib_loop(3))
        self.assertEqual(8, fib.fib_loop(5))
