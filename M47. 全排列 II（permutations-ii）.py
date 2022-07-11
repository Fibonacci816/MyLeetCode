class Solution:
    # dfs回溯
    # 时间O(n×n!) 空间O(n^2)
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        def dfs(nums, path):
            if not nums:
                ans.append(path)
            for i, num in enumerate(nums):
                if i > 0 and nums[i-1] == num:
                    continue
                dfs(nums[:i] + nums[i+1:], path + [num])
        
        dfs(nums, [])
        return ans