class Solution:
    # 滑动窗口
    # 时间O(n) 空间O(n)
    def longestOnes(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans, r = 0, 0
        fliped = set()
        for l in range(n):
            if r < l:
                r = l
            while r < n and (nums[r] == 1 or len(fliped) < k):
                if nums[r] == 0:
                    fliped.add(r)
                r += 1
            ans = max(ans, r - l)
            if l in fliped:
                fliped.remove(l)
        return ans

    # 滑动窗口
    # 时间O(n) 空间O(1)
    def longestOnes(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans, l, cnt = 0, 0, 0
        for r in range(n):
            cnt += 1 - nums[r]
            while l <= r and cnt > k:
                cnt -= 1 - nums[l]
                l += 1
            ans = max(ans, r - l + 1)
        return ans