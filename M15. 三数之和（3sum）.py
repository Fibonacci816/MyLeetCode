class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        left, right = 0, len(nums) - 1
        target = 1
        res = []
        for i in range(n-2):
            # 跳过重复
            if i > 0 and nums[i] == nums[i-1]:
                continue
            target = -nums[i]
            # 左右指针
            left, right = i + 1, n - 1
            # 剪枝
            if nums[left] > target / 2:
                break
            if nums[right] < target / 2:
                continue
            # 双指针相向移动查找
            while left < right:
                if left > i + 1 and nums[left] == nums[left-1]:
                    left += 1
                    continue
                while left < right and nums[left] + nums[right] >= target:
                    if right < n - 1 and nums[right] == nums[right+1]:
                        right -= 1
                        continue
                    if nums[left] + nums[right] == target:
                        res.append([nums[i], nums[left], nums[right]])
                    right -= 1
                left += 1
        return res