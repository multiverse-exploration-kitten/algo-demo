import unittest

from src.l4_tree.basic_nary_tree_patterns import (
    NaryTreeNode,
    post_order_iterative_nary,
    post_order_recursive_nary,
    pre_order_iterative_nary,
    pre_order_recursive_nary,
)


class TestNaryTreeTraversals(unittest.TestCase):
    def setUp(self):
        # Create a sample N-ary tree
        self.root = NaryTreeNode(1)
        self.root.children = [NaryTreeNode(2), NaryTreeNode(3), NaryTreeNode(4)]
        self.root.children[0].children = [NaryTreeNode(5), NaryTreeNode(6)]
        self.root.children[2].children = [NaryTreeNode(7)]

    def test_pre_order_recursive(self):
        result = []
        pre_order_recursive_nary(self.root, result)
        self.assertEqual(result, [1, 2, 5, 6, 3, 4, 7])

    def test_pre_order_iterative(self):
        result = pre_order_iterative_nary(self.root)
        self.assertEqual(result, [1, 2, 5, 6, 3, 4, 7])

    def test_post_order_recursive(self):
        result = []
        post_order_recursive_nary(self.root, result)
        self.assertEqual(result, [5, 6, 2, 3, 7, 4, 1])

    def test_post_order_iterative(self):
        result = post_order_iterative_nary(self.root)
        self.assertEqual(result, [5, 6, 2, 3, 7, 4, 1])


if __name__ == "__main__":
    unittest.main()
