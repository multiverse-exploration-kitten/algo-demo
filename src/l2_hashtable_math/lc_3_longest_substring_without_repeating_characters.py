class Solution:
    def length_of_longest_substring(self, s: str) -> int:
        left = 0
        result = 0
        seen = set()

        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1

            seen.add(s[right])
            result = max(result, right - left + 1)

        return result
