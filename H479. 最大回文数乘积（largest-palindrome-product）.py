class Solution:
    # 枚举
    # 时间O(10^(2n)) 空间O(1)
    def largestPalindrome(self, n: int) -> int:
        if n == 1:
            return 9
        upper = 10 ** n - 1
        lower = upper // 10
        for left in range(upper, lower, -1):
            x = p = left
            while x:
                p = p * 10 + x % 10
                x //= 10
            x = upper
            while x * x >= p:
                if p % x == 0:
                    return p % 1337
                x -= 1