class Solution:
	# dp 状态转移方程：f(n) = max(f(n-2)+nums[n], f(n-1))
    def rob(self, nums: List[int]) -> int:
        f = [0, nums[0]]
        n = len(nums)
        if n < 2:
            return f[n]
        for i in range(1, n):
            f = [f[-1], max(f[0]+ nums[i], f[1])]
        return f[-1]