class Solution:
    # dp
    # 时间O(mn) 空间O(mn)
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n1, n2 = len(text1), len(text2)
        dp = [[0] * n2 for i in range(n1)]
        for i in range(n1):
            for j in range(n2):
                if text1[i] == text2[j]:
                    dp[i][j] = (dp[i-1][j-1] if i > 0 and j > 0 else 0) + 1
                else:
                    dp[i][j] = max(dp[i-1][j] if i > 0 else 0, dp[i][j-1] if j > 0 else 0)
        return dp[-1][-1]
