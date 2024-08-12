import collections


class Solution(object):
    def sumOfDistancesInTree(self, n, edges):
        # Create an adjacency list to represent the tree using a dictionary of sets
        graph = collections.defaultdict(set)

        # Build the graph by adding edges (bidirectional)
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)

        # Initialize count array where count[i] will store the size of the subtree rooted at node i
        # Start with 1 to count the node itself
        count = [1] * n
        # Initialize ans array where ans[i] will store
        # the sum of distances from node i to all other nodes in its subtree
        ans = [0] * n

        # First DFS to calculate the count and initial sum of distances for the root node (assume node 0 is root)
        self.dfs(0, None, graph, count, ans)

        # Second DFS to calculate the final sum of distances for each node based on the root calculations
        self.dfs2(0, None, graph, count, ans, n)

        return ans

    def dfs(self, node, parent, graph, count, ans):
        """
        First DFS to compute:
        1. The size of the subtree rooted at each node (`count` array).
        2. The sum of distances from the root to all nodes in the subtree (`ans` array).

        :param node: The current node being visited
        :param parent: The parent node of the current node (to avoid revisiting)
        :param graph: The adjacency list representing the tree
        :param count: List tracking the size of the subtree rooted at each node
        :param ans: List tracking the sum of distances for each node
        """
        # Explore all the children of the current node
        for child in graph[node]:
            if child != parent:  # Ensure we don't revisit the parent node
                self.dfs(
                    child, node, graph, count, ans
                )  # Recursively perform DFS on the child node

                # After the DFS call returns, we can update the count and ans for the current node
                # Add the size of the child's subtree to the current node's subtree size
                count[node] += count[child]
                # Add the child's sum of distances and size to the current node's sum
                ans[node] += ans[child] + count[child]

    def dfs2(self, node, parent, graph, count, ans, N):
        """
        Second DFS to propagate the sum of distances from the root to all other nodes.
        """
        # Explore all the children of the current node
        for child in graph[node]:
            # Ensure we don't revisit the parent node
            if child != parent:
                # Calculate the sum of distances for the child based on the parent's sum of distances
                # The formula is derived as follows:
                # - When moving from a parent to a child, subtract the size of the child's subtree (count[child])
                #   from the parent's sum of distances, because those nodes are now further away by 1 unit.
                # - Add (N - count[child]) to account for the rest of the tree that is now closer by 1 unit.
                ans[child] = ans[node] - count[child] + N - count[child]

                # Recursively perform DFS on the child node to propagate this calculation
                self.dfs2(child, node, graph, count, ans, N)
