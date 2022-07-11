class Solution:
    # 统计各个数位1出现的次数
    # 时间O(logn) 空间O(1)
    def countDigitOne(self, n: int) -> int:
        # 第k位1出现次数：⌊n / 10^(k+1)⌋ * 10^k + min(max(n % 10^(k+1) − 10^k + 1, 0), 10^k)
        ans = 0
        mul_k = 1
        while n >= mul_k:
            ans += n // (mul_k * 10) * mul_k + min(max(n % (mul_k * 10) - mul_k + 1, 0), mul_k)
            mul_k *= 10
        return ans