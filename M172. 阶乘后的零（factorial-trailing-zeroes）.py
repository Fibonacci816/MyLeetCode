class Solution:
    # [1,n]中p的倍数有(n//p)个， p^k的倍数额外(除去p,p^2,...,p^(k-1)的倍数所贡献的)贡献(n//p^k)个质因子p
    # 时间O(n) 空间O(1)
    def trailingZeroes(self, n: int) -> int:
        ans = 0
        while n:
            n //= 5
            ans += n
        return ans