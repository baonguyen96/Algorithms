import time
import unittest


class UnitTestTemplate(unittest.TestCase):

    def setUp(self):
        self.start = time.time()

    def tearDown(self):
        elapsed = time.time() - self.start
        print('\n{} ({}s)\n'.format(self.id(), round(elapsed, 5)))
