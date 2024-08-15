class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:

        intervals.sort()
        count = 0
        ends = []
        for interval in intervals:
            if len(ends) == 0 or interval[0] < ends[0]:
                count += 1
                heapq.heappush(ends, interval[1])
            else:
                heapq.heappop(ends)
                heapq.heappush(ends, interval[1])
        return count
