class Solution:
    # dfs回溯
    # 时间O(n2^n) 空间O(n2^n)
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(nums, path):
            res.append(path)
            for i in range(len(nums)):
                dfs(nums[i+1:], path+[nums[i]])
        dfs(nums, [])
        return res
    # 添加新数到原有子集元素末尾构成新的子集元素
    # 时间O(n2^n) 空间O(n2^n)
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for num in nums:
            res.extend([s + [num] for s in tmp_set])
        return res
    # 二进制位代表对应元素选不选
    # 时间O(n2^n) 空间O(n2^n)
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        return [[nums[i] for i in range(n) if mask & 1<<i] for mask in range(1<<n)]
