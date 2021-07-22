class Solution:
	# 时间O(n)
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        for num in nums:
            if nums[abs(num)-1] < 0:  # 将第num个数值小于零说明num之前访问过一次，
                res.append(abs(num))
            nums[abs(num)-1] *= -1  # 将第num个数值乘以负一，标记num访问过一次
        return res