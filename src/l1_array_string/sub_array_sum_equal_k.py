# https://leetcode.com/problems/subarray-sum-equals-k/description/
from typing import List


class Solution:
    def subarray_sum(self, nums: List[int], k: int) -> int:
        count, cum_sum = 0, 0
        sums = {0: 1}

        for num in nums:
            cum_sum += num
            count += sums.get(cum_sum - k, 0)
            sums[cum_sum] = sums.get(cum_sum, 0) + 1
        return count
