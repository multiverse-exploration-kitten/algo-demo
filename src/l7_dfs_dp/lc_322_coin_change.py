import sys
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # top down dfs implementation
        return self.dfs(coins, amount, {})

    def dfs(self, coins, amount, memo):

        if amount == 0:
            return 0
        if amount < 0:
            return -1

        if amount in memo:
            return memo[amount]

        curr_min_coin = sys.maxsize

        for coin in coins:
            prev = self.dfs(coins, amount - coin, memo)
            if prev != -1:
                curr_min_coin = min(curr_min_coin, prev + 1)

        if curr_min_coin == sys.maxsize:
            return -1

        memo[amount] = curr_min_coin

        return memo[amount]

    def coin_change_bottom_up(self, coins: List[int], amount: int) -> int:
        # bottom up
        dp = [sys.maxsize for _ in range(amount + 1)]
        dp[0] = 0

        for i in range(amount + 1):
            for coin in coins:
                if i < coin:
                    continue

                dp[i] = min(dp[i], dp[i - coin] + 1)

        if dp[amount] == sys.maxsize:
            return -1

        return dp[amount]

