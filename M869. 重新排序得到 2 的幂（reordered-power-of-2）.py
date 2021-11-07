class Solution:
    # 获取全排列，判断是否是2的幂
    def reorderedPowerOf2(self, n: int) -> bool:
        def get_permutation(s, tmp, n):
            if len(tmp) == n:
                if tmp[0] != '0':
                    if is_pow2(int(tmp)):
                        # print(tmp)
                        return True
                return False
            for i in range(len(s)):
                if get_permutation(s[:i] + s[i+1:], tmp+s[i], n):
                    return True
            return False
        
        def is_pow2(num):
            return not num & (num - 1)

        s = str(n)
        return get_permutation(s, '', len(s))

    # 一个数中0-9每个数字出现的次数决定它是否是2的幂，预存2的幂集合，判断所给数是否在集合内
    def reorderedPowerOf2(self, n: int) -> bool:
        # 统计0-9每个数字出现的次数，返回tuple（list不能被索引）
        # 时间O(logn)（log以10为底）
        def num2tuple(n):
            res = [0] * 10
            while n:
                res[n % 10] += 1
                n //= 10
            return tuple(res)
        all_pow2 = {num2tuple(1 << i) for i in range(30)}  # (2^10)^3 > (10^3)^3
        return num2tuple(n) in all_pow2