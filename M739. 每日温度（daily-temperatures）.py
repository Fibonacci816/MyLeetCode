class Solution:
    # 单调递减栈
    # 时间O(n) 空间O(n)
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ans = [0] * len(temperatures)
        for i, temperature in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temperature:
                j = stack.pop()
                ans[j] = i - j
            stack.append(i)
        return ans
        