class Solution:
    # 中心扩散（每个位置向两边扩展）O(n^2)
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        res = ''
        for i in range(n):
            l = 0
            j = i  # i，j之间的字符都相同
            while j+1 < n and s[j+1] == s[i]:
                j += 1
            while i-l >= 0 and j+l < n:
                if s[i-l] == s[j+l]:
                    tmp = s[i-l:j+l+1]
                else:
                    break
                l += 1
            if len(tmp) > len(res):
                res = tmp
        return res

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