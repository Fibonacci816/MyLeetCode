class Solution:
    # dp
    # 时间O(mn) 空间O(mn)
    def minCost(self, costs: List[List[int]]) -> int:
        n, m = len(costs), len(costs[0])
        dp = [[0] * m for i in range(n)]
        dp[0] = costs[0]
        for i in range(1, n):
            for j in range(m):
                dp[i][j] = costs[i][j] + min(dp[i-1][k] for k in range(m) if k != j)
        return min(dp[n-1])

    # dp + 空间优化
    # 时间O(mn) 空间O(m)
    def minCost(self, costs: List[List[int]]) -> int:
        n, m = len(costs), len(costs[0])
        dp = costs[0]
        for i in range(1, n):
            dp = [c + min(dp[j-k] for k in range(1, m)) for j, c in enumerate(costs[i])]
        return min(dp)