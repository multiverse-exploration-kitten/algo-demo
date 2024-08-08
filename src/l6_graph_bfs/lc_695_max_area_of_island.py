from collections import deque
from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if len(grid) == 0:
            return 0

        seen = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]

        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and not seen[i][j]:
                    island_size = self.explore(grid, seen, i, j)

                    res = max(res, island_size)

        return res

    def explore(self, grid, seen, i, j):
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        q = deque([(i, j)])
        seen[i][j] = True
        size = 0

        while q:
            x, y = q.popleft()

            size += 1

            for dx, dy in directions:
                new_x, new_y = x + dx, y + dy
                if not self.in_bound(new_x, new_y, grid):
                    continue
                if seen[new_x][new_y]:
                    continue
                if grid[new_x][new_y] == 0:
                    continue

                q.append((new_x, new_y))
                seen[new_x][new_y] = True

        return size

    def in_bound(self, x, y, grid):
        return 0 <= x < len(grid) and 0 <= y < len(grid[0])
