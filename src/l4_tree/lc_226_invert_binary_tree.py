from typing import Optional

from src.l4_tree.basic_binary_tree_patterns import TreeNode


class Solution:
    def invert_tree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return

        # pre-order traversal

        # process root
        root.left, root.right = root.right, root.left

        # process left
        self.invert_tree(root.left)
        # process right
        self.invert_tree(root.right)

        return root
