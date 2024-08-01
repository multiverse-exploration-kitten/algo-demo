class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# Recursive Pre-order Traversal
def pre_order_recursive(node, result):
    if not node:
        return
    result.append(node.value)
    pre_order_recursive(node.left, result)
    pre_order_recursive(node.right, result)


# Iterative Pre-order Traversal
def pre_order_iterative(pre_order_root):
    if not pre_order_root:
        return []
    result = []
    stack = [pre_order_root]
    while stack:
        node = stack.pop()
        result.append(node.value)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return result


# Recursive In-order Traversal
def in_order_recursive(node, result):
    if not node:
        return
    in_order_recursive(node.left, result)
    result.append(node.value)
    in_order_recursive(node.right, result)


# Iterative In-order Traversal
def in_order_iterative(in_order_iterative_root):
    result, stack = [], []
    current = in_order_iterative_root
    while stack or current:
        while current:
            stack.append(current)
            current = current.left
        current = stack.pop()
        result.append(current.value)
        current = current.right
    return result


# Recursive Post-order Traversal
def post_order_recursive(node, result):
    if not node:
        return
    post_order_recursive(node.left, result)
    post_order_recursive(node.right, result)
    result.append(node.value)


# Iterative Post-order Traversal
def post_order_iterative(post_order_iterative_root):
    if not post_order_iterative_root:
        return []
    result, stack = [], [(post_order_iterative_root, False)]
    while stack:
        node, visited = stack.pop()
        if not node:
            continue
        if visited:
            result.append(node.value)
        else:
            stack.append((node, True))
            if node.right:
                stack.append((node.right, False))
            if node.left:
                stack.append((node.left, False))
    return result


if __name__ == "__main__":
    # Create a sample tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    # Recursive traversal results
    pre_order_res = []
    in_order_res = []
    post_order_res = []

    pre_order_recursive(root, pre_order_res)
    in_order_recursive(root, in_order_res)
    post_order_recursive(root, post_order_res)

    print("Recursive Pre-order:", pre_order_res)
    print("Recursive In-order:", in_order_res)
    print("Recursive Post-order:", post_order_res)

    # Iterative traversal results
    print("Iterative Pre-order:", pre_order_iterative(root))
    print("Iterative In-order:", in_order_iterative(root))
    print("Iterative Post-order:", post_order_iterative(root))
