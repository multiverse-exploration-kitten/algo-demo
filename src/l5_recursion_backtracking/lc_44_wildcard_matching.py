class Solution:
    def is_match(self, s: str, p: str) -> bool:
        # memoization -> remove duplications -> save calculated results
        return self.dfs(s, 0, p, 0, {})

    def dfs(self, s, s_idx, p, p_idx, memo):
        if (s_idx, p_idx) in memo:
            return memo[(s_idx, p_idx)]

        if len(s) == s_idx:
            # base case 1 str finishes first
            for idx in range(p_idx, len(p)):
                if p[idx] != "*":
                    return False

            return True

        if len(p) == p_idx:
            # base case 2, pattern finishes first
            return False

        if p[p_idx] != "*":
            # case 1, if pattern is not a star.
            # str must match pattern
            matched = self.is_equal(s[s_idx], p[p_idx]) and self.dfs(
                s, s_idx + 1, p, p_idx + 1, memo
            )
        else:
            # case 2, if pattern is a star.
            # star could represent 0 or 1 character for current level
            matched = self.dfs(s, s_idx, p, p_idx + 1, memo) or self.dfs(
                s, s_idx + 1, p, p_idx, memo
            )

        memo[(s_idx, p_idx)] = matched

        return matched

    def is_equal(self, s, p):
        if s == p:
            return True
        if p == "?":
            return True

        return False
