from time import perf_counter


# bottom-up / tabulation DP
def fib_dp(n):
    dp = [0 for _ in range(n + 1)]
    dp[0] = 0
    dp[1] = 1
    # [0, 1, 1, 2, 3, 5, 8, 13]
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


# top-down DP #memoization
def _fib_dfs_with_memo(n, memo):
    if n == 0:
        return 0

    if n == 1:
        return 1

    if n in memo:
        return memo[n]

    memo[n] = _fib_dfs_with_memo(n - 1, memo) + _fib_dfs_with_memo(n - 2, memo)
    return memo[n]


def fib_with_memo(n):
    return _fib_dfs_with_memo(n, {})


def fib_dfs(n):
    if n == 0:
        return 0

    if n == 1:
        return 1

    return fib_dfs(n - 1) + fib_dfs(n - 2)


if __name__ == "__main__":
    # 1 1 2 3 5 8 13 21 34 55
    # 1 2 3 4 5 6 7  8  9  10
    # fib(10) = fib(8) + fib(9)
    # fib(9) = fib(7) + fib(8)
    # fib(8) = fib(6) + fib(7)
    start = perf_counter()
    print(fib_dp(39))
    stop_1 = perf_counter()
    print(fib_with_memo(39))
    stop_2 = perf_counter()
    print(fib_dfs(39))
    stop_3 = perf_counter()
    print(f"fib_dp: {stop_1 - start}")
    print(f"fib_with_memo: {stop_2 - stop_1}")
    print(f"fib_dfs: {stop_3 - stop_2}")
