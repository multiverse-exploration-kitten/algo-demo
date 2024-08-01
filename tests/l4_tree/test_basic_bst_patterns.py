import unittest

from src.l4_tree.basic_bst_patterns import (
    BSTNode,
    deserialize,
    find_max,
    find_min,
    find_predecessor,
    find_successor,
    serialize,
)


class TestBSTFunctions(unittest.TestCase):
    def setUp(self):
        # Create a sample BST
        self.root = BSTNode(10)
        self.root.left = BSTNode(5)
        self.root.right = BSTNode(15)
        self.root.left.left = BSTNode(2)
        self.root.left.right = BSTNode(7)
        self.root.right.left = BSTNode(12)
        self.root.right.right = BSTNode(20)

    def test_find_min(self):
        self.assertEqual(find_min(self.root), 2)

    def test_find_max(self):
        self.assertEqual(find_max(self.root), 20)

    def test_find_predecessor(self):
        self.assertEqual(
            find_predecessor(self.root, self.root.right.left), 10
        )  # 12's predecessor is 10
        self.assertEqual(
            find_predecessor(self.root, self.root.left), 2
        )  # 5's predecessor is 2
        self.assertIsNone(
            find_predecessor(self.root, self.root.left.left)
        )  # 2's predecessor is None

    def test_find_successor(self):
        self.assertEqual(
            find_successor(self.root, self.root.left), 7
        )  # 5's successor is 7
        self.assertEqual(
            find_successor(self.root, self.root.right.left), 15
        )  # 12's successor is 15
        self.assertIsNone(
            find_successor(self.root, self.root.right.right)
        )  # 20's successor is None

    def test_serialize_deserialize(self):
        data = serialize(self.root)
        deserialized_root = deserialize(data)
        self.assertEqual(serialize(deserialized_root), data)


if __name__ == "__main__":
    unittest.main()
