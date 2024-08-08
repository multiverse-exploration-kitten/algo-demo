# solution with bfs
import collections
from typing import List


class SolutionWithBFS:
    def num_islands(self, grid: List[List[str]]) -> int:
        cnt = 0

        visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "0":
                    continue

                if visited[i][j]:
                    continue

                self.visit(i, j, grid, visited)
                cnt += 1

        return cnt

    def visit(self, x, y, grid, visited):
        visited[x][y] = True

        q = collections.deque([(x, y)])

        deltas = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        while q:
            x, y = q.popleft()

            for dx, dy in deltas:
                nx = x + dx
                ny = y + dy
                if not self.in_bound(nx, ny, grid):
                    continue

                if visited[nx][ny]:
                    continue

                if grid[nx][ny] == "0":
                    continue

                q.append((nx, ny))
                visited[nx][ny] = True

    def in_bound(self, x, y, grid):
        return 0 <= x < len(grid) and 0 <= y < len(grid[0])


# solution with union find
class UnionFind:
    def __init__(self, grid):
        self.count = 0
        m, n = len(grid), len(grid[0])
        self.parent = [-1] * (m * n)
        self.rank = [0] * (m * n)
        # Initialize parent for each '1' cell and count them
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    self.parent[i * n + j] = i * n + j
                    self.count += 1

    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, x, y):
        rootx = self.find(x)
        rooty = self.find(y)
        if rootx != rooty:
            if self.rank[rootx] > self.rank[rooty]:
                self.parent[rooty] = rootx
            elif self.rank[rootx] < self.rank[rooty]:
                self.parent[rootx] = rooty
            else:
                self.parent[rooty] = rootx
                self.rank[rootx] += 1
            self.count -= 1


class SolutionWithUnionFind:
    def num_islands(self, grid):
        if not grid or not grid[0]:
            return 0

        m, n = len(grid), len(grid[0])
        uf = UnionFind(grid)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    grid[i][j] = "0"  # Mark as visited
                    for x, y in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                        if 0 <= x < m and 0 <= y < n and grid[x][y] == "1":
                            uf.union(i * n + j, x * n + y)

        return uf.count
