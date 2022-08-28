class Solution:
    # dp
    # 时间O(mn) 空间O(n)
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0]:
            return 0
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [0] * n
        dp[0] = 1
        for i in range(m):
            for j in range(n):
                dp[j] = 0 if obstacleGrid[i][j] else dp[j] + (dp[j-1] if j > 0 else 0)
        return dp[-1]