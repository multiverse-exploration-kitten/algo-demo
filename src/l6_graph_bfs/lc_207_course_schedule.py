import collections
from typing import List


class Solution:
    def can_finish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        in_degree = [0 for _ in range(numCourses)]
        edges = {i: [] for i in range(numCourses)}

        for i, j in prerequisites:
            in_degree[i] += 1
            edges[j].append(i)

        starting_courses = [i for i, c in enumerate(in_degree) if c == 0]

        q = collections.deque(starting_courses)

        cnt = 0
        while q:
            curr_course = q.popleft()
            cnt += 1

            for c in edges[curr_course]:
                in_degree[c] -= 1
                if in_degree[c] == 0:
                    q.append(c)

        return cnt == numCourses
