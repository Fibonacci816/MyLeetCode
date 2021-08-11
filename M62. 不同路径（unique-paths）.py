class Solution:
	# 动态规划
	# 时间O(mn) 空间O(mn)
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * n for i in range(m)]
        dp[0][0] = 1
        for i in range(m):
            for j in range(n):
                if i > 0:
                    dp[i][j] += dp[i-1][j]
                if j > 0:
                    dp[i][j] += dp[i][j-1]
        return dp[m-1][n-1]

    # 动态规划 + 空间压缩
    # 时间O(mn) 空间O(n)
    def uniquePaths2(self, m: int, n: int) -> int:
        dp = [1] * n
        for i in range(1, m):
            for j in range(1, n):
                dp[j] += dp[j-1]
        return dp[n-1]

    # 计算组合数
    def uniquePaths3(self, m: int, n: int) -> int:
        return comb(m + n - 2, n - 1)