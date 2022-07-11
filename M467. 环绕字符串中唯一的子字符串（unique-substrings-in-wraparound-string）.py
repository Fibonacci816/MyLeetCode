class Solution:
    # dp[α]表示p中以字符α结尾且在s中的子串的最长长度
    # 时间O(n) 空间O(∣Σ∣) ∣Σ∣=26
    def findSubstringInWraproundString(self, p: str) -> int:
        dp = defaultdict(int)
        k = 1
        for i, c in enumerate(p):
            if i > 0 and (ord(c) - ord(p[i-1])) % 26 == 1:
                k += 1
            else:
                k = 1
            dp[c] = max(dp[c], k)

        return sum(dp.values())
