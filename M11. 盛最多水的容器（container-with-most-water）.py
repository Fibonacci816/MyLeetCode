class Solution:
    # 双指针（两边向中间）
    # 时间O(n) 空间O(1)
    def maxArea(self, height: List[int]) -> int: 
        left, right = 0, len(height) - 1
        res = 0
        while left < right:
            h = min(height[left], height[right])
            w = right - left
            res = max(res, w * h)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return res