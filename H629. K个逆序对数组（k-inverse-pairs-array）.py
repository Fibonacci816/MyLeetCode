class Solution:
    # 时间O(n^2·k) 空间O(k)
    def kInversePairs(self, n: int, k: int) -> int:
        mod = 10**9 + 7
        dp = [0] * (k+1)
        dp[0] = 1
        for i in range(1, n+1):
            for j in range(k, -1, -1):
                dp[j] = sum(dp[j-d] if j-d >= 0 else 0 for d in range(i))
                if dp[j] > mod:
                    dp[j] -= mod
                elif dp[j] < 0:
                    dp[j] += mod
        return dp[k]

    # 时间O(nk) 空间O(nk)（可通过交替使用两个长度为k+1的数组降低空间复杂度为O(k)）
    def kInversePairs(self, n: int, k: int) -> int:
        mod = 10**9 + 7
        dp = [[0] * (k + 1) for _ in range(n+1)]
        dp[0][0] = 1
        for i in range(1, n+1):
            for j in range(k+1):
                dp[i][j] = (dp[i][j-1] if j - 1 >= 0 else 0) - (dp[i-1][j-i] if i - 1 >= 0 and j - i >= 0 else 0) + (dp[i-1][j] if i - 1 >= 0 else 0)
                if dp[i][j] > mod:
                    dp[i][j] -= mod
                elif dp[i][j] < 0:
                    dp[i][j] += mod
        return dp[n][k]