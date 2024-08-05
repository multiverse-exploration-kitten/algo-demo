class Solution:
    def word_pattern_match(self, pattern: str, s: str) -> bool:

        return self.dfs(pattern, s, {}, set())

    def dfs(self, p, s, mapping, used):
        if not p:
            return not s

        char = p[0]
        if char in mapping:
            # get the pattern matched string previously
            word = mapping[char]
            if not s.startswith(word):
                return False

            return self.dfs(p[1:], s[len(word) :], mapping, used)

        for i in range(len(s)):
            word = s[: i + 1]
            if word in used:
                continue

            mapping[char] = word
            used.add(word)

            if self.dfs(p[1:], s[i + 1 :], mapping, used):
                return True

            del mapping[char]
            used.remove(word)

        return False
