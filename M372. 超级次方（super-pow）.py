class Solution:
    # 快速幂
    def superPow(self, a: int, b: List[int]) -> int:
        res = 1
        MOD = 1337
        for p in b[::-1]:
            res = res * pow(a, p, MOD) % MOD
            a = pow(a, 10, MOD)
        return res