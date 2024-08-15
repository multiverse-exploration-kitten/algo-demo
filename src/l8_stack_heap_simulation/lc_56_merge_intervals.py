class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda x: x[0])

        res = []

        last_interval = None

        for interval in intervals:
            if not last_interval or last_interval[1] < interval[0]:
                res.append(interval)
                last_interval = interval
            else:
                last_interval[1] = max(interval[1], last_interval[1])

        return res
