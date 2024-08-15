# max sliding window

import heapq
from collections import Counter


def max_sliding_window(nums, k):
    if not nums:
        return []

    max_heap = []
    result = []

    for i in range(len(nums)):
        heapq.heappush(max_heap, (-nums[i], i))

        if i >= k - 1:
            while max_heap[0][1] <= i - k:
                heapq.heappop(max_heap)
            result.append(-max_heap[0][0])

    return result


# k closest points to origin


def k_closest(points, k):
    max_heap = []

    for x, y in points:
        dist = -(x**2 + y**2)
        if len(max_heap) < k:
            heapq.heappush(max_heap, (dist, x, y))
        else:
            heapq.heappushpop(max_heap, (dist, x, y))

    return [(x, y) for (dist, x, y) in max_heap]


# rearrange string
# Rearrange characters in a string so that no two adjacent characters are the same.
def rearrange_string(s):
    counter = Counter(s)
    max_heap = [(-freq, char) for char, freq in counter.items()]
    heapq.heapify(max_heap)

    prev_freq, prev_char = 0, ""
    result = []

    while max_heap:
        freq, char = heapq.heappop(max_heap)
        result.append(char)

        if prev_freq < 0:
            heapq.heappush(max_heap, (prev_freq, prev_char))

        prev_freq, prev_char = freq + 1, char

    return "".join(result) if len(result) == len(s) else ""
