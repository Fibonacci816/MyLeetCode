class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        left, right = 0, 0
        s = 0
        ans = float('inf')
        # 滑动窗口查找
        for left in range(n):
            while right < n and s < target:
                s += nums[right]
                right += 1
            if s >= target:
                ans = min(ans, right - left)
            s -= nums[left]
        return 0 if ans == float('inf') else ans