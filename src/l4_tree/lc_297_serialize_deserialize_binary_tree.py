from collections import deque

from src.l4_tree.basic_binary_tree_patterns import TreeNode


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if root is None:
            return ""

        q = deque([root])
        res = [str(root.val)]
        while q:
            node = q.popleft()
            if node.left:
                res.append(str(node.left.val))
                q.append(node.left)
            else:
                res.append("#")

            if node.right:
                res.append(str(node.right.val))
                q.append(node.right)
            else:
                res.append("#")

        return ",".join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if data == "":
            return None

        q = deque(data.split(","))

        root = TreeNode(q.popleft())
        q2 = deque([root])

        while q and q2:
            node = q2.popleft()
            curr = q.popleft()
            if curr != "#":
                left_node = TreeNode(curr)
                node.left = left_node
                q2.append(left_node)
            curr = q.popleft()
            if curr != "#":
                right_node = TreeNode(curr)
                node.right = right_node
                q2.append(right_node)

        return root
