import heapq
from typing import List


class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        # Create events for the building starts and ends
        events = []
        for left, right, height in buildings:
            # Building starts
            events.append((left, -height, right))
            # Building ends
            events.append((right, 0, 0))

        # Sort events: by position, then by height (starting before ending)
        events.sort()

        # Result list to store the skyline
        result = []
        # Max-heap to store the active buildings' heights
        live_buildings = [(0, float("inf"))]  # (negative height, right position)

        for position, neg_height, right in events:
            # Remove the past buildings from the heap
            while live_buildings[0][1] <= position:
                heapq.heappop(live_buildings)

            if neg_height:
                # This is a start of a building
                heapq.heappush(live_buildings, (neg_height, right))

            max_height = -live_buildings[0][0]

            # If the current max height is different from the last point in result, add it
            if not result or result[-1][1] != max_height:
                result.append([position, max_height])

        return result
