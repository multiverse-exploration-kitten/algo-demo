# https://leetcode.com/problems/wiggle-sort-ii/description/
import random
from typing import List


class Solution:
    def wiggle_sort(self, nums: List[int]) -> None:
        n = len(nums)
        mid = self.find_medium(nums, n // 2)

        # Three-way partitioning
        i, j, k = 0, 0, n - 1
        while j <= k:
            if nums[j] > mid:
                nums[j], nums[k] = nums[k], nums[j]
                k -= 1
            elif nums[j] < mid:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j += 1
            else:
                j += 1

        # Interleave the elements to maintain the wiggle condition
        if n % 2 == 0:
            mid = n // 2 - 1
        else:
            mid = n // 2

        temp1 = nums[: mid + 1]
        temp2 = nums[mid + 1 :]

        for i in range(len(temp1)):
            nums[2 * i] = temp1[-1 - i]
        for i in range(len(temp2)):
            nums[2 * i + 1] = temp2[-1 - i]

    def find_medium(self, nums, k):
        left, right = 0, len(nums) - 1
        while True:
            pivot_index = random.randint(left, right)
            pivot_index = self.partition(nums, left, right, pivot_index)

            if k == pivot_index:
                return nums[k]
            elif k < pivot_index:
                right = pivot_index - 1
            else:
                left = pivot_index + 1

    def partition(self, nums, left, right, pivot_index):
        pivot = nums[pivot_index]
        nums[pivot_index], nums[right] = nums[right], nums[pivot_index]
        store_index = left

        for i in range(left, right):
            if nums[i] < pivot:
                nums[store_index], nums[i] = nums[i], nums[store_index]
                store_index += 1

        nums[right], nums[store_index] = nums[store_index], nums[right]
        return store_index
