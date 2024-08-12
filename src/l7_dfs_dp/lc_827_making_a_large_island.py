class Solution(object):
    def largestIsland(self, grid):
        n = len(grid)
        area = {}
        index = 2

        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    area[index] = self.dfs(grid, r, c, index, n)
                    index += 1

        ans = max(area.values() or [0])
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 0:
                    seen = {
                        grid[nr][nc]
                        for nr, nc in self.get_neighbors(r, c, n)
                        if grid[nr][nc] > 1
                    }
                    ans = max(ans, 1 + sum(area[i] for i in seen))
        return ans

    def get_neighbors(self, r, c, n):
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        neighbors = []
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < n:
                neighbors.append((nr, nc))
        return neighbors

    def dfs(self, grid, r, c, index, n):
        ans = 1
        grid[r][c] = index
        for nr, nc in self.get_neighbors(r, c, n):
            if grid[nr][nc] == 1:
                ans += self.dfs(grid, nr, nc, index, n)
        return ans
