from collections import deque


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def clone_graph(self, node: Node) -> Node | None:
        if node is None:
            return None
        root = node
        seen = set()

        q = deque([root])
        mapping = dict()

        while q:
            node = q.popleft()

            if node in seen:
                continue

            seen.add(node)
            mapping[node] = Node(node.val)

            for n in node.neighbors:
                q.append(n)

        q = deque([root])
        seen = set()
        while q:
            node = q.popleft()
            if node in seen:
                continue

            seen.add(node)

            new_node = mapping[node]

            for n in node.neighbors:
                q.append(n)
                new_node.neighbors.append(mapping[n])

        return mapping[root]
