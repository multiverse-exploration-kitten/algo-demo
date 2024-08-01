from typing import Optional

from src.l4_tree.basic_binary_tree_patterns import TreeNode


class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        while root:
            self.stack.append(root)
            root = root.left

    def next(self) -> int:
        nxt_node = self.stack[-1]

        if nxt_node.right is not None:
            curr_node = nxt_node.right
            while curr_node:
                self.stack.append(curr_node)
                curr_node = curr_node.left
        else:
            curr_node = self.stack.pop()
            while self.stack and self.stack[-1].right == curr_node:
                curr_node = self.stack.pop()

        return nxt_node.val

    def hasNext(self) -> bool:
        return len(self.stack) > 0
