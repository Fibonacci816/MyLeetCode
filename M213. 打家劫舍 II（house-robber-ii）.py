class Solution:
    # dp
    # 时间O(n) 空间O(1)
    def rob(self, nums: List[int]) -> int:
        def _rob(begin, end):
            first, second = nums[begin], max(nums[begin], nums[begin+1])
            for i in range(begin+2, end):
                first, second = second, max(second, first + nums[i])
            return second
        n = len(nums)
        return nums[0] if n == 1 else max(nums) if n == 2 else max(_rob(0, n-1), _rob(1, n))