import heapq
from typing import List


class Solution:
    def alien_order(self, words: List[str]) -> str:
        # convert implicit graph into
        # explicit graph
        graph = {}
        for word in words:
            for c in word:
                if c not in graph:
                    graph[c] = set()

        for i in range(len(words) - 1):
            curr_word_len = len(words[i])
            nxt_word_len = len(words[i + 1])
            for j in range(min(curr_word_len, nxt_word_len)):
                if words[i][j] != words[i + 1][j]:
                    graph[words[i][j]].add(words[i + 1][j])
                    break

                if j == min(curr_word_len, nxt_word_len) - 1:
                    if len(words[i]) > len(words[i + 1]):
                        return ""

        # calculate in-degrees
        in_degrees = {node: 0 for node in graph}

        for node in graph:
            for neighbor in graph[node]:
                in_degrees[neighbor] += 1

        # topological sort
        q = [node for node in graph if in_degrees[node] == 0]

        # use heapq here to achieve lexicographically order
        heapq.heapify(q)
        alien_order = []

        while q:
            c = heapq.heappop(q)
            alien_order.append(c)
            for edge in graph[c]:
                in_degrees[edge] -= 1
                if in_degrees[edge] == 0:
                    heapq.heappush(q, edge)

        if len(alien_order) == len(graph):
            return "".join(alien_order)

        return ""
