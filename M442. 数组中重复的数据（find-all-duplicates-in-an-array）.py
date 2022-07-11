class Solution:
    # 用符号位做标记
	# 时间O(n) 空间O(1)
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        for num in nums:
            if nums[abs(num)-1] < 0:  # 将第num个数值小于零说明num之前被访问过
                res.append(abs(num))
            nums[abs(num)-1] *= -1  # 将第num个数值乘以负一，标记num被访问过
        return res

    # 用下标做标记（通过交换改变下标）
    # 时间O(n) 空间O(1)
    def findDuplicates(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            while nums[i] != nums[nums[i]-1]:
                nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]
        return [num for i, num in enumerate(nums) if num - 1 != i]
