class Solution:
	# 时间O(n) 空间O(n)
    def longestPalindrome(self, s: str) -> int:
        c_num = defaultdict(int)
        for c in s:
            c_num[c] += 1
        res = 0
        for c in c_num:
            res += c_num[c] // 2 * 2
        return res + 1 if res < len(s) else res