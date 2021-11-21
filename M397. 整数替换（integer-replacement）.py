class Solution:
    # 递归
    # 时间O(logn) 空间O(logn)
    @lru_cache(None)
    def integerReplacement(self, n: int) -> int:
        if n == 1:
            return 0
        if n & 1:
            return 2 + min(self.integerReplacement(n >> 1), self.integerReplacement((n >> 1) + 1))
        else:
            return 1 + self.integerReplacement(n >> 1)
            