from typing import Optional

from src.l4_tree.basic_binary_tree_patterns import TreeNode


class Solution:
    def path_sum(self, root: Optional[TreeNode], target_sum: int) -> int:
        return self.dfs(root, target_sum, 0, {0: 1})

    def dfs(self, root, ts, prev_sum, record):
        if root is None:
            return 0

        count = 0

        curr_sum = prev_sum + root.val
        diff = curr_sum - ts

        if diff in record:
            count += record[diff]

        if curr_sum in record:
            record[curr_sum] += 1
        else:
            record[curr_sum] = 1

        count += self.dfs(root.left, ts, curr_sum, record)
        count += self.dfs(root.right, ts, curr_sum, record)

        # backtracking
        record[curr_sum] -= 1

        return count
