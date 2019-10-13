from anytree import Node

import SampleInterviewQuestions.tree_traversal as tt
from Test.unit_test_template import UnitTestTemplate


class TreeTraversalTest(UnitTestTemplate):
    @staticmethod
    def get_default_tree():
        udo = Node("Udo")
        marc = Node("Marc", parent=udo)
        lian = Node("Lian", parent=marc)
        dan = Node("Dan", parent=udo)
        jet = Node("Jet", parent=dan)
        jan = Node("Jan", parent=dan)
        joe = Node("Joe", parent=dan)
        return udo

    def test_tree_traversal_empty(self):
        root = None
        expected_path = ''
        actual_path = tt.depth_first_search(root)
        self.assertEqual(expected_path, actual_path)
        actual_path = tt.breadth_first_search(root)
        self.assertEqual(expected_path, actual_path)

    def test_tree_traversal_single(self):
        root = Node('root')
        expected_path = 'root'
        actual_path = tt.depth_first_search(root)
        self.assertEqual(expected_path, actual_path)
        actual_path = tt.breadth_first_search(root)
        self.assertEqual(expected_path, actual_path)

    def test_depth_first_search(self):
        root = TreeTraversalTest.get_default_tree()
        expected_path = 'Lian Marc Jet Jan Joe Dan Udo'
        actual_path = tt.depth_first_search(root)
        self.assertEqual(expected_path, actual_path)

    def test_breadth_first_search(self):
        root = TreeTraversalTest.get_default_tree()
        expected_path = 'Udo Marc Dan Lian Jet Jan Joe'
        actual_path = tt.breadth_first_search(root)
        self.assertEqual(expected_path, actual_path)
