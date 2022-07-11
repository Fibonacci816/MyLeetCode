class Solution:
    # 滑动窗口 + dp
    # 时间O(n) 空间O(n)
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k == 0:
            return 0
        n, product, l = len(nums), 1, 0
        dp = [0] * n
        for r in range(n):
            product *= nums[r]
            while l <= r and product >= k:
                product //= nums[l]
                l += 1
            dp[r] = dp[r-1] + r - l + 1
        return dp[n-1]

    # 滑动窗口 + dp（空间优化）
    # 时间O(n) 空间O(1)
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k == 0:
            return 0
        ans, product, l = 0, 1, 0
        for r in range(len(nums)):
            product *= nums[r]
            while l <= r and product >= k:
                product //= nums[l]
                l += 1
            ans += r - l + 1
        return ans