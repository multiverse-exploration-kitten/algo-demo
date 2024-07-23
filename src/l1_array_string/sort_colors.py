from typing import List


def sort_colors(nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """

    # [0,0,0,1,1,2,2]
    #        L
    #            R
    #          p

    left, right, pivot_idx = 0, len(nums) - 1, 0

    while pivot_idx <= right:
        if nums[pivot_idx] == 0:
            nums[left], nums[pivot_idx] = nums[pivot_idx], nums[left]
            left += 1
            pivot_idx += 1
        elif nums[pivot_idx] == 2:
            nums[right], nums[pivot_idx] = nums[pivot_idx], nums[right]
            right -= 1
        else:
            pivot_idx += 1
