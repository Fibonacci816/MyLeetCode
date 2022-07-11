class Solution:
    # 排列组合
    # 时间O(n) 空间O(1)
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        cnt, cur = 1, 9
        for i in range(n):
            cnt += cur
            cur *= 9 - i
        return cnt
