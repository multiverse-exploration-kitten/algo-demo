from typing import List


class Solution:
    def find_median_of_two_sorted_arrays(
        self, nums1: List[int], nums2: List[int]
    ) -> float:
        if len(nums1) > len(nums2):
            return self.find_median_of_two_sorted_arrays(nums2, nums1)

        m, n = len(nums1), len(nums2)
        left, right = 0, m

        while left <= right:
            partition_a = (left + right) // 2
            partition_b = (m + n + 1) // 2 - partition_a

            max_left_a = float("-inf") if partition_a == 0 else nums1[partition_a - 1]
            min_right_a = float("inf") if partition_a == m else nums1[partition_a]

            max_left_b = float("-inf") if partition_b == 0 else nums2[partition_b - 1]
            min_right_b = float("inf") if partition_b == n else nums2[partition_b]

            if max_left_a <= min_right_b and max_left_b <= min_right_a:
                if (m + n) % 2 == 0:
                    return (
                        max(max_left_a, max_left_b) + min(min_right_a, min_right_b)
                    ) / 2
                else:
                    return max(max_left_a, max_left_b)
            elif max_left_a > min_right_b:
                right = partition_a - 1
            else:
                left = partition_a + 1
