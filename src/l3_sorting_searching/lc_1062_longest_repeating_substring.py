class Solution:
    def longest_repeating_substring(self, s: str) -> int:
        n = len(s)

        left, right = 1, n
        while left <= right:
            mid = left + (right - left) // 2
            if self._search(mid, n, s) != -1:
                left = mid + 1
            else:
                right = mid - 1

        return left - 1

    def _search(self, l: int, n: int, s: str) -> int:
        seen = set()
        for start in range(n - l + 1):
            substring = s[start : start + l]
            if substring in seen:
                return start
            seen.add(substring)
        return -1
