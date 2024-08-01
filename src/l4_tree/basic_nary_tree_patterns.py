class NaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []


# Recursive Pre-order Traversal
def pre_order_recursive_nary(node, result):
    if not node:
        return
    result.append(node.value)
    for child in node.children:
        pre_order_recursive_nary(child, result)


# Iterative Pre-order Traversal
def pre_order_iterative_nary(root):
    if not root:
        return []
    result = []
    stack = [root]
    while stack:
        node = stack.pop()
        result.append(node.value)
        stack.extend(reversed(node.children))
    return result


# Recursive Post-order Traversal
def post_order_recursive_nary(node, result):
    if not node:
        return
    for child in node.children:
        post_order_recursive_nary(child, result)
    result.append(node.value)


# Iterative Post-order Traversal
def post_order_iterative_nary(root):
    if not root:
        return []
    result, stack = [], [(root, False)]
    while stack:
        node, visited = stack.pop()
        if not node:
            continue
        if visited:
            result.append(node.value)
        else:
            stack.append((node, True))
            stack.extend((child, False) for child in reversed(node.children))
    return result
