class Solution:
    # 回溯
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(path):
            if len(path) == len(nums):
                res.append(path)
                return
            for num in nums:
                if num in path:
                    continue
                backtrack(path+[num])  # 等价于进入函数前加入path退出函数后从path删除
        backtrack([])
        return res

    # 递归
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        if n == 1:
            return [nums]
        else:
            res = []
            for i in range(n):
                tmp = self.permute(nums[:i] + nums[i+1:])
                res.extend([[nums[i]] + sub for sub in tmp])
            return res


print(list(itertools.permutations(nums, len(nums))))