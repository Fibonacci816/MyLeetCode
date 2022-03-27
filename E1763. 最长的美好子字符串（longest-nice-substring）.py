class Solution:
    # 时间O(n^2) 空间O(1)
    def longestNiceSubstring(self, s: str) -> str:
        ans = ""
        n = len(s)
        for i in range(n):
            lower_flag = upper_flag = 0
            for j in range(i, n):
                if s[j].islower():
                    lower_flag |= 1 << ord(s[j]) - ord('a')
                else:
                    upper_flag |= 1 << ord(s[j]) - ord('A')
                if lower_flag == upper_flag and j - i + 1 > len(ans):
                    ans = s[i:j+1]
        return ans
