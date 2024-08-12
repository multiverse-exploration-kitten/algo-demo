# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        self.res = []
        self.seen = dict()

        self.traverse(root)

        return self.res

    def traverse(self, node):
        if node is None:
            return "#"

        left = self.traverse(node.left)
        right = self.traverse(node.right)

        sub_tree = f"{left}, {right}, {node.val}"

        if sub_tree in self.seen:
            if self.seen[sub_tree] == 1:
                self.res.append(node)

            self.seen[sub_tree] += 1
            return sub_tree

        self.seen[sub_tree] = 1
        return sub_tree
