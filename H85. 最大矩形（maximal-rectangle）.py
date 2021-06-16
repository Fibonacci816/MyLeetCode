class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        if m == 0:
            return 0
        n = len(matrix[0])
        area = 0
        for start in range(m):
            if (m - start) * n <= area:
                break
            heights = [0] * n
            for i in range(n):
                j = start
                while j < m and matrix[j][i] == '1':
                    heights[i] += 1
                    j += 1
            heights = [-1] + heights + [-1]
            # 单调栈
            stack = [0]
            for i in range(1, n+2):
                while heights[i] < heights[stack[-1]]:
                    h = heights[stack.pop()]
                    w = i - stack[-1] - 1
                    area = max(area, w * h)
                stack.append(i)
        return area