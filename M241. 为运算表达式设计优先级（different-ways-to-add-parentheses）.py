class Solution:
    # dp
    # 时间O(2^n) 空间O(2^n)
    def diffWaysToCompute(self, expression: str) -> List[int]:
        subs = []
        ops = []
        sub = ""
        for i, c in enumerate(expression):
            if c in {'+', '-', '*', '/'}:
                subs.append(int(sub))
                sub = ""
                ops.append(c)
            else:
                sub += c
        subs.append(int(sub))
        assert len(subs) == len(ops) + 1

        @lru_cache
        def dp(l, r):
            if l == r:
                return [subs[l]]
            ans = []
            for i in range(l, r):
                left = dp(l, i)
                right = dp(i+1, r)
                for x in left:
                    for y in right:
                        ans.append(eval(f"x {ops[i]} y"))
            return ans
        
        return dp(0, len(subs) - 1)