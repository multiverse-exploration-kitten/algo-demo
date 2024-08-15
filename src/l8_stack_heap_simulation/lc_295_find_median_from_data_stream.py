import heapq


class MedianFinder:

    def __init__(self):
        self.max_heap = []
        self.min_heap = []

    def addNum(self, num: int) -> None:
        max_heap_len = len(self.max_heap)
        min_heap_len = len(self.min_heap)

        if self.max_heap and num < -self.max_heap[0]:
            heapq.heappush(self.max_heap, -num)
        elif self.min_heap and num > self.min_heap[0]:
            heapq.heappush(self.min_heap, num)
        else:
            if max_heap_len < min_heap_len:
                heapq.heappush(self.max_heap, -num)
            else:
                heapq.heappush(self.min_heap, num)

        self.rebalance()

    def rebalance(self):
        max_heap_len = len(self.max_heap)
        min_heap_len = len(self.min_heap)

        if max_heap_len > min_heap_len:
            if max_heap_len - min_heap_len > 1:
                num_to_move = -heapq.heappop(self.max_heap)
                heapq.heappush(self.min_heap, num_to_move)
        else:
            if min_heap_len - max_heap_len > 1:
                num_to_move = heapq.heappop(self.min_heap)
                heapq.heappush(self.max_heap, -num_to_move)

    def findMedian(self) -> float:
        max_heap_len = len(self.max_heap)
        min_heap_len = len(self.min_heap)

        if max_heap_len == min_heap_len:
            median = (self.min_heap[0] - self.max_heap[0]) / 2
        else:
            if max_heap_len > min_heap_len:
                median = -self.max_heap[0]
            else:
                median = self.min_heap[0]

        return median
