import collections
import heapq
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        heap = []
        res = 0

        for k, v in collections.Counter(tasks).items():
            heapq.heappush(heap, -v)

        while heap:
            i, tmp = 0, []

            while i <= n:
                res += 1

                if heap:
                    curr_task = heapq.heappop(heap)
                    if curr_task != -1:
                        curr_task += 1
                        tmp.append(curr_task)
                if heap or tmp:
                    i += 1
                else:
                    break

            for task in tmp:
                heapq.heappush(heap, task)

        return res
