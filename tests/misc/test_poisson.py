from src.misc.poisson import create_poisson_problem_nza, sparse_mv_mult
from tests.unit_test_template import UnitTestTemplate
import src.utilities.utility as util


class PoissonTest(UnitTestTemplate):

    def test_create_poisson_problem_nza_2(self):
        nza, ir, ic = create_poisson_problem_nza(2)
        self.assertEqual(nza, [4, -1, -1, -1, 4, -1, -1, 4, -1, -1, -1, 4])
        self.assertEqual(ir, [1, 4, 7, 10, 13])
        self.assertEqual(ic, [1, 2, 3, 1, 2, 4, 1, 3, 4, 2, 3, 4])

    def test_create_poisson_problem_nza_3(self):
        nza, ir, ic = create_poisson_problem_nza(3)
        self.assertEqual(nza, [4, -1, -1, -1, 4, -1, -1, -1, 4, -1, -1, 4, -1, -1, -1, -1, 4, -1, -1, -1, -1, 4, -1, -1, 4, -1, -1, -1, 4, -1, -1, -1, 4])
        self.assertEqual(ir, [1, 4, 8, 11, 15, 20, 24, 27, 31, 34])
        self.assertEqual(ic, [1, 2, 4, 1, 2, 3, 5, 2, 3, 6, 1, 4, 5, 7, 2, 4, 5, 6, 8, 3, 5, 6, 9, 4, 7, 8, 5, 7, 8, 9, 6, 8, 9])

    def test_sparse_mv_mult(self):
        nza = [4, -1, -1, -1, 4, -1, -1, 4, -1, -1, -1, 4]
        ir = [1, 4, 7, 10, 13]
        ic = [1, 2, 3, 1, 2, 4, 1, 3, 4, 2, 3, 4]
        x = [9, 10, 6, 8]
        y = sparse_mv_mult(nza, ir, ic, x)
        self.assertEqual(y, [20, 23, 7, 16])
