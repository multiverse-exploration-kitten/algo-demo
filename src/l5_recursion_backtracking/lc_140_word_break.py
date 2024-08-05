from typing import List


class Solution:
    def word_break(self, s: str, wd: List[str]) -> List[str]:

        return self.dfs(s, wd, {})

    def dfs(self, s, wd, memo):
        if s in memo:
            return memo[s]

        if len(s) == 0:
            return []

        partitions = []

        for i in range(1, len(s)):
            prefix = s[:i]

            if prefix not in wd:
                continue

            sub_partitions = self.dfs(s[i:], wd, memo)
            for p in sub_partitions:
                partitions.append(prefix + " " + p)

        if s in wd:
            partitions.append(s)

        memo[s] = partitions

        return partitions
