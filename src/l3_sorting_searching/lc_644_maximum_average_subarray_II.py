from typing import List


class Solution:
    def find_max_average(self, nums: List[int], k: int) -> float:
        start, end = min(nums), max(nums)

        while end - start > 1e-5:
            mid = (start + end) / 2
            if self.check_subarray(nums, k, mid):
                start = mid
            else:
                end = mid

        return start

    def check_subarray(self, nums, k, average):
        prefix_sum = [0]

        for num in nums:
            prefix_sum.append(prefix_sum[-1] + num - average)

        min_prefix_sum = 0

        for i in range(k, len(nums) + 1):
            if prefix_sum[i] - min_prefix_sum >= 0:
                return True

            min_prefix_sum = min(min_prefix_sum, prefix_sum[i - k + 1])

        return False
