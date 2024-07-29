from typing import List


class MergeSort:
    def sort_array(self, nums: List[int]) -> List[int]:
        tmp = [0 for _ in range(len(nums))]

        self.ms(0, len(nums) - 1, nums, tmp)
        return nums

    def ms(self, start, end, nums, tmp):
        if start >= end:
            return

        mid = (start + end) // 2

        self.ms(start, mid, nums, tmp)
        self.ms(mid + 1, end, nums, tmp)
        self.merge(start, mid, end, nums, tmp)

    def merge(self, start, mid, end, nums, tmp):
        left, right = start, mid + 1
        idx = start

        while left <= mid and right <= end:
            if nums[left] <= nums[right]:
                tmp[idx] = nums[left]
                left += 1
            else:
                tmp[idx] = nums[right]
                right += 1
            idx += 1

        while left <= mid:
            tmp[idx] = nums[left]
            left += 1
            idx += 1

        while right <= end:
            tmp[idx] = nums[right]
            right += 1
            idx += 1

        for i in range(start, end + 1):
            nums[i] = tmp[i]
