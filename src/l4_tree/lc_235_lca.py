from src.l4_tree.basic_binary_tree_patterns import TreeNode


class Solution:
    def lca(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode | None:
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return None

        if root == p or root == q:
            return root

        left_find = self.lca(root.left, p, q)
        right_find = self.lca(root.right, p, q)

        if left_find and right_find:
            return root

        if left_find:
            return left_find
        if right_find:
            return right_find

        return None
