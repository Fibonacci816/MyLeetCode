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

    # 双指针（相向移动）
    # 时间O(n) 空间O(1)
    def trap(self, height: List[int]) -> int:
        ans = 0
        left, right = 0, len(height) - 1
        leftMax = rightMax = 0  # 左指针左边最高的柱子和右指针右边最高的柱子
        while left < right:
            leftMax = max(leftMax, height[left])
            rightMax = max(rightMax, height[right])
            # 移动指向较短柱子的指针
            if height[left] < height[right]:
                ans += leftMax - height[left]
                left += 1
            else:
                ans += rightMax - height[right]
                right -= 1   
        return ans

    # 两次遍历存储状态，再遍历一次统计结果
    # 时间O(n) 空间O(n)
    def trap(self, height: List[int]) -> int:
        n = len(height)
        leftMax = [0] * n
        rightMax = [0] * n
        for i in range(n):
            leftMax[i] = max(height[i], leftMax[i-1]) if i > 0 else height[i]
        for i in range(n-1, -1, -1):
            rightMax[i] = max(height[i], rightMax[i+1]) if i < n-1 else height[i]
        return sum(max(min(leftMax[i], rightMax[i]) - height[i] , 0) for i in range(n))

    # 单调栈
    # 时间O(n) 空间O(n)
    def trap(self, height: List[int]) -> int:
        ans = 0
        stack = []
        for i in range(len(height)):
            while stack and height[i] > height[stack[-1]]:
                cur_height = height[stack.pop()]
                if not stack:
                    break
                w = i - stack[-1] - 1
                h = min(height[i], height[stack[-1]]) - cur_height
                ans += w * h
            stack.append(i)
        return ans