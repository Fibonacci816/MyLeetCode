class Solution:
    def twoSum(self, nums, start, end, target):
        ans = []
        while start < end:
            if nums[start] + nums[end] < target:
                start += 1
            elif nums[start] + nums[end] > target:
                end -= 1
            else:
                ans.append([start, end])
                while start < end and nums[start] == nums[start + 1]:
                    start += 1
                while start < end and nums[end] == nums[end - 1]:
                    end -= 1
                start += 1
                end -= 1
        return ans

        
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        ans = []
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i + 1, n):
                if j > i + 1 and nums[j] == nums[j-1]:
                    continue
                ans_tow_sum = self.twoSum(nums, j + 1, n - 1, target - nums[i] - nums[j])
                for k, l in ans_tow_sum:
                    ans.append([nums[i], nums[j], nums[k], nums[l]])
        return ans