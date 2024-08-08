from collections import defaultdict, deque

# represent a graph using an adjacency list.
graph_adjacency_list = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B"],
    "E": ["B", "F"],
    "F": ["C", "E"],
}


# represent a graph using an adjacency matrix.
graph_adjacency_matrix = [
    [0, 1, 1, 0, 0, 0],
    [1, 0, 0, 1, 1, 0],
    [1, 0, 0, 0, 0, 1],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 1],
    [0, 0, 1, 0, 1, 0],
]


# Example usage
# edges = [(0, 1), (0, 2), (1, 2), (2, 3)]
# graph = build_graph_from_edges(edges)
def build_graph_from_edges(edges):

    graph = {}
    for u, v in edges:
        if u not in graph:
            graph[u] = []
        if v not in graph:
            graph[v] = []
        graph[u].append(v)
        graph[v].append(u)  # For directed graph, remove this line
    return graph


def build_graph_from_matrix(matrix):
    graph = {}
    for i in range(len(matrix)):
        graph[i] = []
        for j in range(len(matrix[i])):
            if matrix[i][j] == 1:
                graph[i].append(j)
    return graph


# graph traversal using depth first search.
def graph_traverse_dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    for neighbor in graph[start]:
        if neighbor not in visited:
            graph_traverse_dfs(graph, neighbor, visited)
    return visited


# graph traversal using breadth first search.
def bfs(graph, start):
    visited = set()
    queue = deque([start])
    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            visited.add(vertex)
            queue.extend(set(graph[vertex]) - visited)
    return visited


# topological sort
def topological_sort(graph):
    in_degree = defaultdict(int)
    for node in graph:
        for neighbor in graph[node]:
            in_degree[neighbor] += 1

    queue = deque([node for node in graph if in_degree[node] == 0])
    topo_order = []

    while queue:
        node = queue.popleft()
        topo_order.append(node)
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    if len(topo_order) == len(graph):
        return topo_order
    else:
        return []  # Graph has a cycle


# shortest path using breadth first search
def shortest_path(graph, start, goal):
    queue = deque([(start, [start])])
    visited = set()
    while queue:
        vertex, path = queue.popleft()
        if vertex == goal:
            return path
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))
    return None


# BFS in a Grid (Shortest Path, Flood Fill, etc.):
def bfs_in_grid(grid, start):
    rows, cols = len(grid), len(grid[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    queue = deque([start])
    visited = set()
    visited.add(start)
    while queue:
        row, col = queue.popleft()
        for dr, dc in directions:
            r, c = row + dr, col + dc
            if 0 <= r < rows and 0 <= c < cols and (r, c) not in visited:
                if grid[r][c] == 1:  # Example condition, e.g., walkable cell
                    queue.append((r, c))
                    visited.add((r, c))
    return visited
