class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# Find minimum value in a BST
def find_min(node):
    while node.left:
        node = node.left
    return node.value


# Find maximum value in a BST
def find_max(node):
    while node.right:
        node = node.right
    return node.value


# Find in-order predecessor in a BST
def find_predecessor(root, node):
    if node.left:
        return find_max(node.left)
    predecessor = None
    while root:
        if node.value > root.value:
            predecessor = root
            root = root.right
        elif node.value < root.value:
            root = root.left
        else:
            break
    return predecessor.value if predecessor else None


# Find in-order successor in a BST
def find_successor(root, node):
    if node.right:
        return find_min(node.right)
    successor = None
    while root:
        if node.value < root.value:
            successor = root
            root = root.left
        elif node.value > root.value:
            root = root.right
        else:
            break
    return successor.value if successor else None


def serialize(root):
    result = []
    serialize_helper(root, result)
    return " ".join(result)


def serialize_helper(node, result):
    if not node:
        result.append("#")
        return
    result.append(str(node.value))
    serialize_helper(node.left, result)
    serialize_helper(node.right, result)


def deserialize(data):
    values = iter(data.split())
    return deserialize_helper(values)


def deserialize_helper(values):
    val = next(values)
    if val == "#":
        return None
    node = BSTNode(int(val))
    node.left = deserialize_helper(values)
    node.right = deserialize_helper(values)
    return node
