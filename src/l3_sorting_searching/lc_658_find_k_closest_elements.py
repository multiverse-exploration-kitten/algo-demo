from typing import List


class Solution:
    def find_closest_elements(self, arr: List[int], k: int, x: int) -> List[int]:
        left, right = 0, len(arr) - 1

        while left + 1 < right:
            mid = (left + right) // 2
            if arr[mid] < x:
                left = mid
            else:
                right = mid

        dist_left = abs(arr[left] - x)
        dist_right = abs(arr[right] - x)

        if dist_left <= dist_right:
            pivot = left
        else:
            pivot = right

        if pivot == 0:
            return arr[:k]
        elif pivot == len(arr) - 1:
            return arr[-k:]
        else:
            lo = max(0, pivot - k)
            hi = min(len(arr) - 1, pivot + k)
            while hi - lo > k - 1:
                if abs(x - arr[lo]) <= abs(x - arr[hi]):
                    hi -= 1
                else:
                    lo += 1

        return arr[lo: hi + 1]
