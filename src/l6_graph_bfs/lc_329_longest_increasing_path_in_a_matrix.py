import collections
from typing import List


# solution with topological sort
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        in_degree = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]

        deltas = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        for x in range(len(matrix)):
            for y in range(len(matrix[0])):
                for dx, dy in deltas:
                    new_x = x + dx
                    new_y = y + dy
                    if not self.in_bound(new_x, new_y, matrix):
                        continue

                    if matrix[new_x][new_y] < matrix[x][y]:
                        in_degree[x][y] += 1

        q = collections.deque([])
        for x in range(len(matrix)):
            for y in range(len(matrix[0])):
                if in_degree[x][y] == 0:
                    q.append((x, y))

        res = 0

        while q:
            for _ in range(len(q)):
                x, y = q.popleft()
                for dx, dy in deltas:
                    nx, ny = x + dx, y + dy

                    if not self.in_bound(nx, ny, matrix):
                        continue

                    if matrix[nx][ny] > matrix[x][y]:
                        in_degree[nx][ny] -= 1
                        if in_degree[nx][ny] == 0:
                            q.append((nx, ny))

            res += 1

        return res

    def in_bound(self, x, y, matrix):
        return 0 <= x < len(matrix) and 0 <= y < len(matrix[0])


# solution with dfs
class SolutionWithDFS:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:

        if not matrix:
            return 0
        self.m, self.n = len(matrix), len(matrix[0])
        cache = [[0] * self.n for _ in range(self.m)]
        ans = 0
        for i in range(self.m):
            for j in range(self.n):
                ans = max(ans, self.dfs(matrix, i, j, cache))
        return ans

    def dfs(self, matrix, i, j, cache):
        if cache[i][j] != 0:
            return cache[i][j]

        self.dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for d in self.dirs:
            x, y = i + d[0], j + d[1]
            if 0 <= x < self.m and 0 <= y < self.n and matrix[x][y] > matrix[i][j]:
                cache[i][j] = max(cache[i][j], self.dfs(matrix, x, y, cache))
        cache[i][j] += 1
        return cache[i][j]
