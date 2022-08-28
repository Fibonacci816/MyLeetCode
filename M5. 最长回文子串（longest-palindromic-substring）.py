class Solution:
    # 中心扩散（每个位置向两边扩展）O(n^2)
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        start, max_len = 0, 0
        for i in range(n):
            j = i
            while j + 1 < n and s[i] == s[j+1]:
                j += 1
            l = 1
            while i - l >= 0 and j + l < n and s[i-l] == s[j+l]:
                l += 1
            cur_len = j + l - (i - l) - 1
            if cur_len > max_len:
                start = i - l + 1
                max_len = cur_len
        return s[start:start+max_len]

    # 动态规划O(n^2)
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[True] * n for i in range(n)]
        begin = 0
        max_len = 1
        for j in range(1, n):
            for i in range(j):
                dp[i][j] = s[i] == s[j] and (j - i < 3 or dp[i+1][j-1])
                if dp[i][j] and j - i + 1 > max_len:
                    begin = i
                    max_len = j - i + 1
        return s[begin:begin+max_len]