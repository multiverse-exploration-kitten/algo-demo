import sys

from src.l4_tree.basic_binary_tree_patterns import TreeNode


class Solution:
    def find_bottom_left_value(self, root: TreeNode) -> int:
        self.res = 0
        self.max_len = -sys.maxsize
        self.dfs(root, 0)
        return self.res

    def dfs(self, root, left_len):

        if root.left is None and root.right is None:
            if left_len > self.max_len:
                self.max_len = left_len
                self.res = root.val
            return

        if root.left:
            self.dfs(root.left, left_len + 1)

        if root.right:
            self.dfs(root.right, left_len + 1)

        return
