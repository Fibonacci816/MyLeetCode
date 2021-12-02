class Solution:
    # 时间O(n) 空间O(1)
    def maxPower(self, s: str) -> int:
        res = cnt = 1
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                cnt += 1
                res = max(res, cnt)
            else:
                cnt = 1
        return res