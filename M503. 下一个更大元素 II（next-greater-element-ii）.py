class Solution:
    # 单调递减栈
    # 时间O(n) 空间O(n)
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [-1] * n
        stack = []
        for i, num in enumerate(nums * 2):
            while stack and nums[stack[-1]] < num:
                ans[stack.pop()] = num
            stack.append(i % n)
        return ans
