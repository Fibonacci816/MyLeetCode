class Solution:
    # 每次配对淘汰一人，需淘汰n-1人
    def numberOfMatches(self, n: int) -> int:
        return n - 1

    def numberOfMatches(self, n: int) -> int:
        ans = 0
        while n > 1:
            ans += n >> 1
            n = (n >> 1) + (n & 1)
        return ans
