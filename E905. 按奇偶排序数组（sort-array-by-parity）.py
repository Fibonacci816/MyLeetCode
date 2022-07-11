class Solution:
    # 遍历 + 原地交换
    # 时间O(n) 空间O(1)
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        idx = -1
        for i, num in enumerate(nums):
            if num & 1 == 0:
                idx += 1
                nums[idx], nums[i] = nums[i], nums[idx]
        return nums