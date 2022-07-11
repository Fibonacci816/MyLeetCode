class Solution:
    # 暴力穷举
    # 时间O(n^2) 空间O(1)
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans = 0
        for l in range(len(nums)):
            _sum = 0
            for r in range(l, len(nums)):
                _sum += nums[r]
                if _sum == k:
                    ans += 1
        return ans

    # 哈希表 + 前缀和
    # 时间O(n) 空间O(n)
    def subarraySum(self, nums: List[int], k: int) -> int:
        sum_cnt = defaultdict(int)
        sum_cnt[0] = 1
        ans, pre = 0, 0
        for num in nums:
            pre += num
            if pre - k in sum_cnt:
                ans += sum_cnt[pre-k]
            sum_cnt[pre] += 1
        return ans