from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left + 1 < right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] >= nums[left]:
                if nums[left] <= target < nums[mid]:
                    right = mid
                else:
                    left = mid + 1
            else:
                if nums[right] >= target > nums[mid]:
                    left = mid
                else:
                    right = mid - 1

        if nums[left] == target:
            return left

        if nums[right] == target:
            return right

        return -1
