class Solution:
    # dp递归
    # 时间O(n^2) 空间O(n^2)（递归栈最大深度O(n)，但记忆空间为O(n^2)）
    def getMoneyAmount(self, n: int) -> int:
        @lru_cache(20000)
        def dp(i, j):
            if i == j:
                return 0
            if i == j - 1:
                return i
            if i == j - 2:
                return i + 1
            # if i == j - 3:
            #     return i + i + 2
            # if i == j - 4:
            #     return i + 1 + i + 3
            # if i == j - 5:
            #     return i + 2 + i + 4
            # if i == j - 6:
            #     return i + 3 + i + 5
            return min(k + max(dp(i, k-1), dp(k+1, j)) for k in range(i + 1, j))
        return dp(1, n)

    # 思路同上，时间空间复杂度同上，简化代码
    def getMoneyAmount(self, n: int) -> int:
        @lru_cache(20000)
        def dp(i, j):
            if i >= j:
                return 0
            return min(k + max(dp(i, k-1), dp(k+1, j)) for k in range(i, j))
        return dp(1, n)

    # dp迭代
    # 时间O(n^2) 空间O(n^2)
    def getMoneyAmount(self, n: int) -> int:
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        for i in range(n - 1, 0, -1):
            for j in range(i + 1, n + 1):
                dp[i][j] = min(k + max(dp[i][k-1], dp[k+1][j]) for k in range(i, j))
        return dp[1][n]