from typing import List


class Solution:
    def count_range_sum(self, nums: List[int], lower: int, upper: int) -> int:
        prefix_sum = [0]
        for n in nums:
            prefix_sum.append(prefix_sum[-1] + n)

        return self._mergesort(prefix_sum, lower, upper, 0, len(prefix_sum) - 1)

    def _mergesort(
        self, prefix_sum: List[int], lower: int, upper: int, left: int, right: int
    ) -> int:
        if left == right:
            return 0

        mid = (left + right) // 2
        count = self._mergesort(prefix_sum, lower, upper, left, mid) + self._mergesort(
            prefix_sum, lower, upper, mid + 1, right
        )

        i = j = mid + 1
        for left_value in prefix_sum[left : mid + 1]:
            while i <= right and prefix_sum[i] - left_value < lower:
                i += 1
            while j <= right and prefix_sum[j] - left_value <= upper:
                j += 1
            count += j - i

        prefix_sum[left : right + 1] = sorted(prefix_sum[left : right + 1])
        return count
