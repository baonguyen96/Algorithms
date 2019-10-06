from SampleInterviewQuestions.lowest_common_ancestor import get_lowest_common_ancestor
from Test.unit_test_template import UnitTestTemplate


class LowestCommonAncestorTest(UnitTestTemplate):
    tree = [1, 3, 2, 4, 6, None, None, None, None, 5]

    def test_get_lowest_common_ancestor_4_5(self):
        i1 = LowestCommonAncestorTest.tree.index(4)
        i2 = LowestCommonAncestorTest.tree.index(5)
        lca_index, lca_value = get_lowest_common_ancestor(LowestCommonAncestorTest.tree, i1, i2)
        self.assertEqual(1, lca_index)
        self.assertEqual(3, lca_value)

    def test_get_lowest_common_ancestor_for_3_and_5(self):
        i1 = LowestCommonAncestorTest.tree.index(3)
        i2 = LowestCommonAncestorTest.tree.index(5)
        lca_index, lca_value = get_lowest_common_ancestor(LowestCommonAncestorTest.tree, i1, i2)
        self.assertEqual(1, lca_index)
        self.assertEqual(3, lca_value)

    def test_get_lowest_common_ancestor_for_4_and_2(self):
        i1 = LowestCommonAncestorTest.tree.index(4)
        i2 = LowestCommonAncestorTest.tree.index(2)
        lca_index, lca_value = get_lowest_common_ancestor(LowestCommonAncestorTest.tree, i1, i2)
        self.assertEqual(0, lca_index)
        self.assertEqual(1, lca_value)

    def test_get_lowest_common_ancestor_for_6_and_6(self):
        i1 = LowestCommonAncestorTest.tree.index(6)
        i2 = LowestCommonAncestorTest.tree.index(6)
        lca_index, lca_value = get_lowest_common_ancestor(LowestCommonAncestorTest.tree, i1, i2)
        self.assertEqual(4, lca_index)
        self.assertEqual(6, lca_value)
