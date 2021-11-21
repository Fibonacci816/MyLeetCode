class Solution:
    # 排序+hash（记录每个数字的次数）
    # 时间O(nlogn) 空间O(n)
    def findLHS(self, nums: List[int]) -> int:
        nums.sort()
        num_count = OrderedDict()
        n = len(nums)
        cnt = 1
        for i in range(n):
            if i < n - 1 and nums[i] == nums[i+1]:
                cnt += 1
            else:
                num_count[nums[i]] = cnt
                cnt = 1
        k_pre = v_pre = None
        res = 0
        for k, v in num_count.items():
            if k_pre is not None and k == k_pre + 1:
                res = max(res, v_pre + v)
            k_pre, v_pre = k, v
        return res

    # 用Counter简化代码，思路同上
    # 时间O(nlogn) 空间O(n)
    def findLHS(self, nums: List[int]) -> int:
        num_count = Counter(nums)
        num_count = sorted((k, v) for k, v in num_count.items())
        k_pre = v_pre = None
        res = 0
        for k, v in num_count:
            if k_pre is not None and k == k_pre + 1:
                res = max(res, v_pre + v)
            k_pre, v_pre = k, v
        return res

    # 用Counter，不排序，遍历k，v时判断k+1是否存在
    # 时间O(nlogn) 空间O(n)
    def findLHS(self, nums: List[int]) -> int:
        num_count = Counter(nums)
        return max([v + num_count[k+1] for k, v in num_count.items() if k+1 in num_count], default=0)