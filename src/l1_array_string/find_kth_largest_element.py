from typing import List


class Solution:
    def find_kth_largest(self, nums: List[int], k: int) -> int:
        return self.qs(nums, k - 1, 0, len(nums) - 1)

    def qs(self, nums, k, start, end):
        if start >= end:
            return nums[k]

        mid = (start + end) // 2
        pivot = nums[mid]

        left, right = start, end

        while left <= right:
            while left <= right and pivot < nums[left]:
                left += 1
            while left <= right and pivot > nums[right]:
                right -= 1

            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        if k >= left:
            return self.qs(nums, k, left, end)
        if k <= right:
            return self.qs(nums, k, start, right)

        return nums[k]
