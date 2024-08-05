from typing import List


class Solution:
    def solve_n_queens(self, n: int) -> List[List[str]]:
        boards = [["." for _ in range(n)] for _ in range(n)]
        res = []
        self.dfs(boards, n, 0, res)
        return res

    def dfs(self, boards, n, row, res):

        if n == row:
            tmp = []
            for row in boards:
                tmp.append("".join(row))
            res.append(tmp)
            return

        for i in range(n):
            if not self.is_valid(boards, i, row):
                continue

            boards[row][i] = "Q"
            self.dfs(boards, n, row + 1, res)
            boards[row][i] = "."

    def is_valid(self, boards, col, row):

        # up
        for i in range(row - 1, -1, -1):
            if boards[i][col] == "Q":
                return False

        # top left
        i = row - 1
        j = col - 1

        while i >= 0 and j >= 0:
            if boards[i][j] == "Q":
                return False
            i -= 1
            j -= 1

        # top right
        i = row - 1
        j = col + 1

        while i >= 0 and j < len(boards[0]):
            if boards[i][j] == "Q":
                return False
            i -= 1
            j += 1

        return True
