import sys

from src.l4_tree.basic_binary_tree_patterns import TreeNode


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.ans = -sys.maxsize
        self.dfs(root)
        return self.ans

    def dfs(self, root: TreeNode):
        if root is None:
            return 0

        left_max = max(self.dfs(root.left), 0)
        right_max = max(self.dfs(root.right), 0)
        curr_node_sum = root.value + left_max + right_max
        self.ans = max(self.ans, curr_node_sum)

        return root.value + max(left_max, right_max)
