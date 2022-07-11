class Solution:
    # 哈希表
    # 时间O(n) 空间O(n)
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        ans = 0
        for num in num_set:
            # 当num-1 存在时， 从num-1开始的连续序列长度一定大于从num开始的连续序列长度
            if num - 1 not in num_set:
                cur = num + 1
                while cur in num_set:
                    cur += 1
                ans = max(ans, cur - num)
        return ans
