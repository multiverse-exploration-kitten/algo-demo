from typing import List


class Solution:
    def min_cost(self, nums: List[int], cost: List[int]) -> int:
        n = len(nums)
        nums_cost_pairs = sorted(zip(nums, cost))

        # Binary search to find the optimal target
        left, right = min(nums), max(nums)
        while left < right:
            mid = (left + right) // 2

            if self.compute_cost(nums_cost_pairs, mid) < self.compute_cost(
                nums_cost_pairs, mid + 1
            ):
                right = mid
            else:
                left = mid + 1

        # Compute cost for the final target value
        return self.compute_cost(nums_cost_pairs, left)

    def compute_cost(self, nums_cost_pairs, target):
        left, right = 0, len(nums_cost_pairs)
        while left < right:
            mid = left + (right - left) // 2
            if nums_cost_pairs[mid][0] <= target:
                left = mid + 1
            else:
                right = mid

        # Calculate the cost using the sorted nums_cost_pairs
        cost_left = sum(
            (target - nums_cost_pairs[i][0]) * nums_cost_pairs[i][1]
            for i in range(left)
        )
        cost_right = sum(
            (nums_cost_pairs[i][0] - target) * nums_cost_pairs[i][1]
            for i in range(left, len(nums_cost_pairs))
        )
        return cost_left + cost_right
