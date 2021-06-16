class Solution:
    # 划分数组，求每个子数组的乘积，取最大值
    def maxProduct(self, nums: List[int]) -> int:
        def get_product(nums):
            if not nums:
                return 0
            res = 1
            for num in nums:
                res *= num
            return res

        n = len(nums)
        sub_nums = []  # nums以0分割为子数组
        minus_idx = []  # 存放所有子数组中负数的位置
        tmp_nums = []  # 当前子数组
        tmp_idx = []  # 当前子数组中负数的位置
        start_idx = 0 # 子数组的当前位置
        max_product = -inf  # 乘积最大子数组的乘积
        # 分割nums
        for i in range(n): 
            if nums[i] != 0:
                tmp_nums.append(nums[i])
                if nums[i] < 0:
                    tmp_idx.append(start_idx)
                start_idx += 1
            if nums[i] == 0 or i == n-1:
                sub_nums.append(tmp_nums)
                minus_idx.append(tmp_idx)
            if nums[i] == 0:
                tmp_nums = []
                tmp_idx = []
                start_idx = 0
                max_product = 0
        # 计算每个子数组的乘积，并找到最大乘积
        for i in range(len(sub_nums)):
            if sub_nums[i] == []:
                continue
            if len(minus_idx[i]) % 2:
                if len(sub_nums[i]) == 1:
                    product = sub_nums[i][0]
                else:
                    product1 = get_product(sub_nums[i][minus_idx[i][0]+1:]) 
                    product2 = get_product(sub_nums[i][:minus_idx[i][-1]])
                    product = max(product1, product2)
            else:
                product = get_product(sub_nums[i])
            max_product = max(max_product, product)
        return max_product

    # 动态规划
    def maxProduct2(self, nums: List[int]) -> int:
        res = minF = maxF = nums[0]  # 第 i 个元素结尾的乘积最小/最大子数组的乘积
        for num in nums[1:]:
            minF, maxF = min(minF * num, maxF * num, num), max(minF * num, maxF * num, num)
            res = max(res, maxF)
        return res
