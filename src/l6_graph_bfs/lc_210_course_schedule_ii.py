from collections import deque
from typing import List


class Solution:
    def find_order(self, num_courses: int, prerequisites: List[List[int]]) -> List[int]:
        in_degree = [0 for _ in range(num_courses)]
        edges = {i: [] for i in range(num_courses)}

        for i, j in prerequisites:
            in_degree[i] += 1
            edges[j].append(i)

        start_course = [i for i, c in enumerate(in_degree) if c == 0]

        q = deque(start_course)

        res = []
        while q:
            curr_course = q.popleft()
            res.append(curr_course)

            for c in edges[curr_course]:
                in_degree[c] -= 1
                if in_degree[c] == 0:
                    q.append(c)

        if len(res) != num_courses:
            return []

        return res
