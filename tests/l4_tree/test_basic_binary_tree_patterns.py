import unittest

from src.l4_tree.basic_binary_tree_patterns import (
    TreeNode,
    in_order_iterative,
    in_order_recursive,
    post_order_iterative,
    post_order_recursive,
    pre_order_iterative,
    pre_order_recursive,
)


class TestTreeTraversals(unittest.TestCase):
    def setUp(self):
        # Create a sample tree
        self.root = TreeNode(1)
        self.root.left = TreeNode(2)
        self.root.right = TreeNode(3)
        self.root.left.left = TreeNode(4)
        self.root.left.right = TreeNode(5)

    def test_pre_order_recursive(self):
        result = []
        pre_order_recursive(self.root, result)
        self.assertEqual(result, [1, 2, 4, 5, 3])

    def test_pre_order_iterative(self):
        result = pre_order_iterative(self.root)
        self.assertEqual(result, [1, 2, 4, 5, 3])

    def test_in_order_recursive(self):
        result = []
        in_order_recursive(self.root, result)
        self.assertEqual(result, [4, 2, 5, 1, 3])

    def test_in_order_iterative(self):
        result = in_order_iterative(self.root)
        self.assertEqual(result, [4, 2, 5, 1, 3])

    def test_post_order_recursive(self):
        result = []
        post_order_recursive(self.root, result)
        self.assertEqual(result, [4, 5, 2, 3, 1])

    def test_post_order_iterative(self):
        result = post_order_iterative(self.root)
        self.assertEqual(result, [4, 5, 2, 3, 1])


if __name__ == "__main__":
    unittest.main()
