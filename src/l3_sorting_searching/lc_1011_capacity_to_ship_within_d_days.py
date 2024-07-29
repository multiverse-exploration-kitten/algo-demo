from typing import List


class Solution:
    def ship_within_d_days(self, weights: List[int], days: int) -> int:
        # Define the search space
        left, right = max(weights), sum(weights)

        while left < right:
            mid = left + (right - left) // 2
            current_weight = 0
            days_needed = 1

            for weight in weights:
                if current_weight + weight > mid:
                    days_needed += 1
                    current_weight = 0
                current_weight += weight

            if days_needed > days:
                left = mid + 1
            else:
                right = mid

        return left
