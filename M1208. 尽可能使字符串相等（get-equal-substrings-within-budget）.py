class Solution:
    # 滑动窗口
    # 时间O(n) 空间O(1)
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        ans, l, cost = 0, 0, 0
        for r, (c1, c2) in enumerate(zip(s, t)):
            cost += abs(ord(c1) - ord(c2))
            while l <= r and cost > maxCost:
                cost -= abs(ord(s[l]) - ord(t[l]))
                l += 1
            ans = max(ans, r - l + 1)
        return ans
