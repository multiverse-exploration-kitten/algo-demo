import sys
from typing import List


class Solution:
    def find_cheapest_price(
        self, n: "int", flights: List[List[int]], src: int, dst: int, k: int
    ) -> int:
        k_inf_cost = sys.maxsize
        cost = [k_inf_cost for _ in range(n)]
        cost[src] = 0

        for i in range(k + 1):
            tmp = list(cost)
            for p in flights:
                tmp[p[1]] = min(tmp[p[1]], cost[p[0]] + p[2])
            cost = tmp

        return -1 if cost[dst] >= sys.maxsize else cost[dst]
