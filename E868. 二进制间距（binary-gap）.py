class Solution:
    # 遍历二进制位
    # 时间O(logn) 空间O(1)
    def binaryGap(self, n: int) -> int:
        ans, pre, i = 0, -1, 0
        while n:
            if n & 1:
                if pre != -1:
                    ans = max(ans, i - pre)
                pre = i
            n >>= 1
            i += 1
        return ans
