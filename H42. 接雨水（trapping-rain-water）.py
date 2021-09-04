class Solution:
    def get_area(self, stack):
        area = 0
        for h in stack[1:]:
            area += stack[0] - h
        return area

    # 找中间最高的柱子，以此分为两段计算即可
    # 时间O(n) 空间O(n)
    def trap(self, height: List[int]) -> int:
        n = len(height)
        l = 0
        for l in range(n-1):
            if height[l+1] < height[l]:
                break
        r = n
        for r in range(n, l, -1):
            if height[r-1] > height[r-2]:
                break
        height = height[l: r]
        n = len(height)
        if n <= 2:
            return 0
        stack = [height[0]]
        res = 0
        for i in range(1, n):
            if stack[0] > height[i]:
                stack.append(height[i])
            else:
                res += self.get_area(stack)
                stack = [height[i]]
        
        height = stack[::-1]
        n = len(height)
        if n <= 2:
            return res
        stack = [height[0]]
        for i in range(1, n):
            if stack[0] > height[i]:
                stack.append(height[i])
            else:
                res += self.get_area(stack)
                stack = [height[i]]
        return res
         