# Definition for a binary tree node.
import sys
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        nodes = [TreeNode(num) for num in nums + [sys.maxsize]]

        stack = []

        for index, num in enumerate(nums + [sys.maxsize]):
            # 出现递增
            while stack and nums[stack[-1]] < num:
                top = stack.pop()
                # 当前栈顶就是左侧node
                left = nums[stack[-1]] if stack else sys.maxsize
                if left < num:
                    # 是栈顶的右子树
                    nodes[stack[-1]].right = nodes[top]
                else:
                    # 是当前元素的左子树
                    nodes[index].left = nodes[top]

            # 维护递减
            stack.append(index)

        # sys.maxsize 的左child就是整个array的最大
        # 因为sys.maxsize是整个array最后一个元素
        return nodes[-1].left
