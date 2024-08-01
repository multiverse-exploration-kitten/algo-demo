from src.l4_tree.basic_binary_tree_patterns import TreeNode


class Solution:
    def trim_bst(self, root: TreeNode, low: int, high: int) -> TreeNode | None:
        if root is None:
            return root

        if root.value < low:
            right = self.trim_bst(root.right, low, high)
            return right

        if root.value > high:
            left = self.trim_bst(root.left, low, high)
            return left

        root.left = self.trim_bst(root.left, low, high)
        root.right = self.trim_bst(root.right, low, high)

        return root
