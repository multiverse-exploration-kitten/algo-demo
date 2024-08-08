"""
Tarjan’s Algorithm is an efficient method used to find
Strongly Connected Components (SCCs) in a directed graph.
An SCC is a maximal subgraph where every vertex is reachable
from every other vertex in the subgraph.

Key Concepts of Tarjan’s Algorithm:

1.	Discovery Time (disc[]): This keeps track of the time when a node is first visited during the DFS traversal.
2.	Low Time (low[]): This represents the smallest discovery time reachable from a node,
including the node itself and its descendants.
3.	Stack: Keeps track of the current path in the DFS tree.
4.	On Stack: An array to keep track of whether a node is on the stack.

Algorithm Steps:

1.	Initialization: Initialize the discovery and low arrays, a stack to keep track of the nodes,
and an on-stack boolean array.
2.	DFS Traversal: Perform DFS traversal for each unvisited node. During traversal:
•	Assign discovery and low times.
•	Push the node onto the stack.
•	Update the low time based on the successors.
•	If a node’s discovery time is equal to its low time, it means all nodes on the stack up to this node form an SCC.
3.	SCC Detection: Pop nodes from the stack to form the SCC until you reach the current node.
"""


def build_graph(n: int, connections: list):
    """
    Build an adjacency list representation of the graph.

    :param n: Number of nodes
    :param connections: List of connections where each connection is represented by a pair [u, v]
    :return: Adjacency list of the graph
    """
    graph = {i: [] for i in range(n)}
    for u, v in connections:
        graph[u].append(v)
        graph[v].append(u)
    return graph


def dfs(node, graph, discovery_time, low_time, parent, result, time):
    """
    Perform a DFS to find bridges in the graph.

    :param node: Current node being visited
    :param graph: Adjacency list of the graph
    :param discovery_time: Discovery time of each node
    :param low_time: Lowest discovery time reachable from each node
    :param parent: Parent of each node in the DFS tree
    :param result: List to store the bridges
    :param time: Current time in the DFS traversal
    :return: Updated time after DFS traversal of the node
    """
    discovery_time[node] = low_time[node] = time
    time += 1

    for neighbor in graph[node]:
        if discovery_time[neighbor] == -1:  # If neighbor is not visited
            parent[neighbor] = node
            time = dfs(neighbor, graph, discovery_time, low_time, parent, result, time)
            low_time[node] = min(low_time[node], low_time[neighbor])
            if low_time[neighbor] > discovery_time[node]:
                result.append([node, neighbor])
        elif (
            neighbor != parent[node]
        ):  # Update low value of node for parent function calls
            low_time[node] = min(low_time[node], discovery_time[neighbor])

    return time


def critical_connections(n, connections):
    """
    Find all critical connections in the network.

    :param n: Number of nodes
    :param connections: List of connections where each connection is represented by a pair [u, v]
    :return: List of critical connections
    """
    # Build the graph
    graph = build_graph(n, connections)

    # Initialize arrays
    discovery_time = [-1] * n
    low_time = [-1] * n
    parent = [-1] * n
    result = []

    # Initial time
    time = 0

    # Perform DFS from each node (necessary in case the graph is not connected)
    for i in range(n):
        if discovery_time[i] == -1:
            time = dfs(i, graph, discovery_time, low_time, parent, result, time)

    return result


if __name__ == "__main__":
    # Example usage
    # Output: [[1, 3], [3, 4]]
    print(critical_connections(5, [[0, 1], [1, 2], [2, 0], [1, 3], [3, 4]]))
