"""
The Bellman-Ford algorithm is used to find the shortest paths
from a single source vertex to all other vertices in a weighted graph.
It can handle graphs with negative weight edges and can detect negative weight cycles.
"""


class Edge:
    def __init__(self, source, destination, weight):
        self.source = source
        self.destination = destination
        self.weight = weight


def bellman_ford(vertices, edges, source):
    """
    Bellman-Ford algorithm to find the shortest path from a single source to all vertices.

    :param vertices: Number of vertices in the graph
    :param edges: List of Edge objects representing the edges of the graph
    :param source: The source vertex
    :return: List of shortest distances from the source to each vertex and a flag indicating the presence of a negative weight cycle
    """
    # Step 1: Initialize distances from the source to all other vertices as INFINITE
    distance = [float("inf")] * vertices
    distance[source] = 0

    # Step 2: Relax all edges |V| - 1 times
    for _ in range(vertices - 1):
        for edge in edges:
            if (
                distance[edge.source] != float("inf")
                and distance[edge.source] + edge.weight < distance[edge.destination]
            ):
                distance[edge.destination] = distance[edge.source] + edge.weight

    # Step 3: Check for negative-weight cycles
    for edge in edges:
        if (
            distance[edge.source] != float("inf")
            and distance[edge.source] + edge.weight < distance[edge.destination]
        ):
            return distance, True  # Indicates presence of a negative weight cycle

    return distance, False  # No negative weight cycle found


if __name__ == "__main__":
    # Example usage
    edges = [
        Edge(0, 1, -1),
        Edge(0, 2, 4),
        Edge(1, 2, 3),
        Edge(1, 3, 2),
        Edge(1, 4, 2),
        Edge(3, 2, 5),
        Edge(3, 1, 1),
        Edge(4, 3, -3),
    ]
    vertices = 5
    source = 0

    distances, has_negative_cycle = bellman_ford(vertices, edges, source)

    if has_negative_cycle:
        print("Graph contains a negative weight cycle")
    else:
        print("Shortest distances from source vertex:", distances)
