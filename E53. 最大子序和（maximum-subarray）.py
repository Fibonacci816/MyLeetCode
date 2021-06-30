class Solution:
	# 时间O(n) 空间O(1)
    def maxSubArray(self, nums: List[int]) -> int:
        res = -float('inf')
        s = 0
        for num in nums:
            s += num
            res = max(res, s)
            # 这一步是关键，一旦和小于零，那么就应该重新开始累加，因为加一个小于零的数肯定会使结果变小
            if s < 0:
                s = 0
        return res
