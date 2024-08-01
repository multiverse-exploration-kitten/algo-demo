from src.l4_tree.basic_binary_tree_patterns import TreeNode


class Solution:
    def good_nodes(self, root: TreeNode) -> int:
        return self.dfs(root, root.value)

    def dfs(self, node: TreeNode, max_val: int):
        if not node:
            return 0
        # Count this node if it's good
        good = 1 if node.value >= max_val else 0
        # Update the max value on the path to the current node
        max_val = max(max_val, node.value)
        # Continue DFS on the left and right subtrees
        good += self.dfs(node.left, max_val)
        good += self.dfs(node.right, max_val)
        return good
