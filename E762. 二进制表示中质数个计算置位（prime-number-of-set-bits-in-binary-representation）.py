class Solution:
    # 时间O((r-l)(logr)^0.5) 空间O(1)
    def countPrimeSetBits(self, left: int, right: int) -> int:
        def is_prime(x):
            if x < 2:
                return False
            i = 2
            while i * i <= x:
                if x % i == 0:
                    return False
                i += 1
            return True

        return sum(is_prime(x.bit_count()) for x in range(left, right+1))

    # 提前存储所有可能的质数
    # 时间O(r-l) 空间O(1)
    def countPrimeSetBits(self, left: int, right: int) -> int:
        # 665772 = (10100010100010101100)_2，对应质数: 2,3,5,7,11,13,17,19
        return sum(((1 << x.bit_count()) & 665772) != 0 for x in range(left, right + 1))
