class Solution(object):
    def inorder_successor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return root

        self.stack = []
        while root:
            self.stack.append(root)
            root = root.left

        curr_node = self.get_next()
        while self.has_next and curr_node.val != p.val:
            curr_node = self.get_next()

        if self.has_next():
            return self.get_next()
        else:
            return None

    def has_next(
        self,
    ):
        return len(self.stack) > 0

    def get_next(
        self,
    ):
        next_node = self.stack[-1]
        if next_node.right is not None:
            curr_node = next_node.right
            while curr_node:
                self.stack.append(curr_node)
                curr_node = curr_node.left
        else:
            curr_node = self.stack.pop()
            while self.stack and self.stack[-1].right == curr_node:
                curr_node = self.stack.pop()

        return next_node
