class Solution:
	# 时间O(n) 空间O(1)
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse(nums, left, right):
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        n = len(nums)
        for j in range(n-2, -1, -1):
            if nums[j] >= nums[j+1]:
                continue
            for k in range(n-1, j, -1):
                if nums[k] > nums[j]:
                    nums[j], nums[k] = nums[k], nums[j]
                    reverse(nums, j+1, n-1)
                    return
        nums.reverse()
