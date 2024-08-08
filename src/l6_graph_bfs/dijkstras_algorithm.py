"""
Dijkstra’s algorithm is used for finding the shortest paths
from a single source vertex to all other vertices in a graph
with non-negative weights.
"""

import heapq


def dijkstra(graph, start):
    pq = [(0, start)]
    dist = {node: float("inf") for node in graph}
    dist[start] = 0

    while pq:
        current_dist, current_node = heapq.heappop(pq)
        if current_dist > dist[current_node]:
            continue
        for neighbor, weight in graph[current_node]:
            distance = current_dist + weight
            if distance < dist[neighbor]:
                dist[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    return dist
