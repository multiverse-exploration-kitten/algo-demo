import sys
from typing import List


class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        dp = [[0 for _ in range(3)] for _ in range(len(costs) + 1)]

        for idx, house_cost_by_color in enumerate(costs):
            for color_idx, color_cost in enumerate(house_cost_by_color):

                min_cost = sys.maxsize

                for i in range(3):
                    if color_idx == i:
                        continue

                    min_cost = min(min_cost, dp[idx][i] + color_cost)

                dp[idx + 1][color_idx] = min_cost

        return min(dp[-1])
