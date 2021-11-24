class Solution:
    # f(n, m) = (m + f(n-1, m)) % n
    # 时间O(n) 空间O(1)
    def lastRemaining(self, n: int, m: int) -> int:
        # return 0 if n == 1 else (m + self.lastRemaining(n-1, m)) % n  # 递归版本 空间O(n)
        res = 0
        for i in range(1, n):
            res = (m + res) % (i + 1)
        return res