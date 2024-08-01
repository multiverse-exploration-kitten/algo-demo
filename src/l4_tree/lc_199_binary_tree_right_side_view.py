from collections import deque
from typing import List, Optional

from src.l4_tree.basic_binary_tree_patterns import TreeNode


class Solution:
    def right_side_view(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        next_level = deque(
            [
                root,
            ]
        )
        right_side = []

        while next_level:
            # prepare for the next level
            curr_level = next_level
            next_level = deque()

            while curr_level:
                node = curr_level.popleft()

                # add child nodes of the current level
                # in the queue for the next level
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)

            # The current level is finished.
            # Its last element is the rightmost one.
            right_side.append(node.value)

        return right_side
