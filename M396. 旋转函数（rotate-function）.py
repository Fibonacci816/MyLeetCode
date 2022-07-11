class Solution:
    # 暴力
    # 时间O(n^2) 空间O(1)
    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)
        ans = -inf
        for i in range(n):
            _sum = 0
            for j in range(n):
                _sum += j * nums[j-i]
            ans = max(ans, _sum)
        return ans

    # dp
    # 时间O(n) 空间O(n)
    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)
        _sum = sum(nums)
        tmp = [i * num for i, num in enumerate(nums)]
        ans = f = sum(tmp)
        for i in range(1, n):
            tmp[n-i] += (i - 1) * nums[n-i]
            f = f - tmp[n-i] + _sum - nums[n-i]
            ans = max(ans, f)
        return ans

    # dp（优化状态转移）
    # 时间O(n) 空间O(n)
    def maxRotateFunction(self, nums: List[int]) -> int:
        n, _sum = len(nums), sum(nums)
        ans = f = sum([i * num for i, num in enumerate(nums)])
        for i in range(1, n):
            f = f + _sum - n * nums[n-i]
            ans = max(ans, f)
        return ans
