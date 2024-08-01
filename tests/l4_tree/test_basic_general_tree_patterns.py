import unittest

from src.l4_tree.basic_general_tree_patterns import (
    NaryTreeNode,
    level_order_traversal,
    zigzag_level_order_traversal,
)


class TestNaryTreeTraversals(unittest.TestCase):
    def setUp(self):
        self.root = NaryTreeNode(1)
        self.root.children = [NaryTreeNode(2), NaryTreeNode(3), NaryTreeNode(4)]
        self.root.children[0].children = [NaryTreeNode(5), NaryTreeNode(6)]
        self.root.children[2].children = [NaryTreeNode(7)]

    def test_level_order_traversal(self):
        result = level_order_traversal(self.root)
        self.assertEqual(result, [1, 2, 3, 4, 5, 6, 7])

    def test_zigzag_level_order_traversal(self):
        result = zigzag_level_order_traversal(self.root)
        self.assertEqual(result, [[1], [4, 3, 2], [5, 6, 7]])


if __name__ == "__main__":
    unittest.main()
