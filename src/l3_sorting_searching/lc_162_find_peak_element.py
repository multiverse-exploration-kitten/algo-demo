from typing import List


class Solution:
    def find_peak_element(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if nums[mid] > nums[mid + 1] and nums[mid] > nums[mid - 1]:
                return mid
            elif nums[mid + 1] < nums[mid] < nums[mid - 1]:
                right = mid
            else:
                left = mid

        if nums[left] > nums[right]:
            return left
        return right
