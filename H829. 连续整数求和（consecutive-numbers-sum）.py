class Solution:
    # 数学
    # 时间O(√n) 空间O(1)
    def consecutiveNumbersSum(self, n: int) -> int:
        i, ans = 1, 0
        while i * (i + 1) <= 2 * n:
            if i & 1:
                if n % i == 0:
                    ans += 1
            else:
                if n % i and 2 * n % i == 0:
                    ans += 1
            i += 1
        return ans