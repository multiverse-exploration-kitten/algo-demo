from typing import List


def sortColors(self, nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """

    # [0,0,0,1,1,2,2]
    #        L
    #            R
    #          p

    left, right, pivot = 0, len(nums) - 1, 0

    while pivot <= right:
        if nums[pivot] == 0:
            nums[left], nums[pivot] = nums[pivot], nums[left]
            left += 1
            pivot += 1
        elif nums[pivot] == 2:
            nums[right], nums[pivot] = nums[pivot], nums[right]
            right -= 1
        else:
            pivot += 1
