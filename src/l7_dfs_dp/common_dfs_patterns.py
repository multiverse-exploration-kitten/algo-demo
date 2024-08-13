# subset, combination generation
def dfs_subsets(nums, index, path, res):
    res.append(path)
    for i in range(index, len(nums)):
        dfs_subsets(nums, i + 1, path + [nums[i]], res)


def subsets(nums):
    res = []
    dfs_subsets(nums, 0, [], res)
    return res


# palindrome partitioning
def dfs_partition(s, path, res):
    if not s:
        res.append(path[:])
        return
    for i in range(1, len(s) + 1):
        if s[:i] == s[:i][::-1]:
            dfs_partition(s[i:], path + [s[:i]], res)


def partition(s):
    res = []
    dfs_partition(s, [], res)
    return res


# graph coloring
def dfs_bipartite(graph, node, color, colors):
    if node in colors:
        return colors[node] == color
    colors[node] = color
    for neighbor in graph[node]:
        if not dfs_bipartite(graph, neighbor, 1 - color, colors):
            return False
    return True


def is_bipartite(graph):
    colors = {}
    for node in range(len(graph)):
        if node not in colors:
            if not dfs_bipartite(graph, node, 0, colors):
                return False
    return True


# grid, maze
def dfs_maze(maze, x, y, destination, visited):
    if [x, y] == destination:
        return True
    if (x, y) in visited:
        return False
    visited.add((x, y))
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for i, j in directions:
        nx, ny = x, y
        while len(maze) > nx + i >= 0 == maze[nx + i][ny + j] and 0 <= ny + j < len(
            maze[0]
        ):
            nx += i
            ny += j
        if dfs_maze(maze, nx, ny, destination, visited):
            return True
    return False


def has_path(maze, start, destination):
    visited = set()
    return dfs_maze(maze, start[0], start[1], destination, visited)


def dfs_island(grid, x, y, direction, path_signature):
    if not (0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == 1):
        return ""
    grid[x][y] = 0
    path_signature += direction

    deltas = [("D", 1, 0), ("U", -1, 0), ("R", 0, 1), ("L", 0, -1)]

    for dir, dx, dy in deltas:
        path_signature += dfs_island(grid, x + dx, y + dy, dir, "")

    return path_signature + "B"


def num_distinct_islands(grid):
    shapes = set()
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                shape = dfs_island(grid, i, j, "O", "")
                shapes.add(shape)
    return len(shapes)
