class Solution:
    # 从总和里减去其他数
    # 时间O(n) 空间O(n)
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        _sum = (1 + n) * n // 2
        for num in nums:
            _sum -= num
        return _sum

    # 异或运算（相同数字异或结果为0，异或运算可以交换顺序）
    # 时间O(n) 空间O(n)
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        for num in range(n+1):
            res ^= num
        for num in nums:
            res ^= num
        return res