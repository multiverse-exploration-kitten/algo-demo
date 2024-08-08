import heapq
import sys


class Solution:
    def networkDelayTime(self, times, n, k):
        # Create graph
        graph = {i: [] for i in range(1, n + 1)}
        for u, v, w in times:
            graph[u].append((v, w))

        # Initialize distances array with infinity
        distances = {i: sys.maxsize for i in range(1, n + 1)}
        distances[k] = 0

        # Min-heap to use as the priority queue, initialized with (distance, node)
        heap = [(0, k)]

        while heap:
            current_distance, current_node = heapq.heappop(heap)
            if current_distance > distances[current_node]:
                continue

            for neighbor, weight in graph[current_node]:
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(heap, (distance, neighbor))

        # The result is the maximum distance, if all nodes are reachable
        max_distance = max(distances.values())
        return max_distance if max_distance < sys.maxsize else -1
