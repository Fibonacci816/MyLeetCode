class Solution:
    # dfs回溯
    # 时间O(n2^n) 空间O(n2^n)
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(nums, path):
            if path not in res:
                res.append(path)
            for i in range(len(nums)):
                dfs(nums[i+1:], path+[nums[i]])
        dfs(nums, [])
        return res
    # copy再添加新元素
    # 时间O(n2^n) 空间O(n2^n)
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for num in nums:
            tmp_set = res.copy()
            res.extend([s + [num] for s in tmp_set])
        return res
    # 二进制位代表对应元素选不选
    # 时间O(n2^n) 空间O(n2^n)
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        return [[nums[i] for i in range(n) if mask & 1<<i] for mask in range(1<<n)]
