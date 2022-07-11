class Solution:
    # 单调栈
    # 时间O(n) 空间O(n)
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        ans, stack = 0, [-1]
        for i, height in enumerate(heights):
            while heights[stack[-1]] > height:
                h = heights[stack.pop()]
                ans = max(ans, h * (i - stack[-1] - 1))
            stack.append(i)
        return ans