from collections import deque


class NaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []


# Level-order Traversal
def level_order_traversal(root):
    if not root:
        return []
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        result.append(node.value)
        for child in node.children:
            queue.append(child)
    return result


# Zigzag Level-order Traversal
def zigzag_level_order_traversal(root):
    if not root:
        return []
    result = []
    queue = deque([root])
    left_to_right = True
    while queue:
        level_size = len(queue)
        level = []
        for _ in range(level_size):
            node = queue.popleft()
            if left_to_right:
                level.append(node.value)
            else:
                level.insert(0, node.value)
            for child in node.children:
                queue.append(child)
        result.append(level)
        left_to_right = not left_to_right
    return result


# Morris In-order Traversal
# Optional
def morris_in_order_traversal(root):
    result = []
    current = root
    while current:
        if not current.left:
            result.append(current.value)
            current = current.right
        else:
            pre = current.left
            while pre.right and pre.right is not current:
                pre = pre.right
            if not pre.right:
                pre.right = current
                current = current.left
            else:
                pre.right = None
                result.append(current.value)
                current = current.right
    return result
