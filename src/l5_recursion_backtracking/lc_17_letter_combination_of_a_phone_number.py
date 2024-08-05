from typing import List

KEYBOARD = {
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz",
}


class Solution:
    def letter_combinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        results = []
        self.dfs(digits, 0, [], results)

        return results

    def dfs(self, digits, index, chars, results):
        if index == len(digits):
            results.append("".join(chars))
            return

        for letter in KEYBOARD[digits[index]]:
            chars.append(letter)
            self.dfs(digits, index + 1, chars, results)
            chars.pop()
