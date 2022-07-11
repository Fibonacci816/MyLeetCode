class Solution:
    # 时间O(logn) 空间O(1)
    def hasAlternatingBits(self, n: int) -> bool:
        pre = -1
        while n:
            cur = n % 2
            if cur == pre:
                return False
            n //= 2
            pre = cur
        return True

    # 时间O(1) 空间O(1)
    def hasAlternatingBits(self, n: int) -> bool:
        _xor = n ^ (n >> 1)
        return (_xor + 1) & _xor == 0
