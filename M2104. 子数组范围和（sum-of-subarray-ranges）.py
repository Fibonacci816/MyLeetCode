class Solution:
    # 遍历所有子数组
    # 时间O(n) 空间O(1)
    def subArrayRanges(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(n):
            min_num = max_num = nums[i]
            for j in range(i+1, n):
                min_num = min(min_num, nums[j])
                max_num = max(max_num, nums[j])
                ans += max_num - min_num
        return ans

    # 单调栈
    # 时间O(n) 空间O(n)
    def subArrayRanges(self, nums: List[int]) -> int:
        n = len(nums)
        min_stack, max_stack = [], []
        min_left, max_left = [0] * n, [0] * n  # 第i个数左边最近的比他小的数的下标和最近的比他大的数的下标
        for i in range(n):
            while min_stack and nums[min_stack[-1]] > nums[i]:
                min_stack.pop()
            min_left[i] = min_stack[-1] if min_stack else -1
            min_stack.append(i)

            while max_stack and nums[max_stack[-1]] <= nums[i]:
                max_stack.pop()
            max_left[i] = max_stack[-1] if max_stack else -1
            max_stack.append(i)
        
        min_stack, max_stack = [], []
        min_right, max_right = [0] * n, [0] * n  # 第i个数右边最近的比他小的数的下标和最近的比他大的数的下标
        for i in range(n-1, -1, -1):
            while min_stack and nums[min_stack[-1]] >= nums[i]:
                min_stack.pop()
            min_right[i] = min_stack[-1] if min_stack else n
            min_stack.append(i)

            while max_stack and nums[max_stack[-1]] < nums[i]:
                max_stack.pop()
            max_right[i] = max_stack[-1] if max_stack else n
            max_stack.append(i)

        min_sum = max_sum = 0  # 所有子数组的最小值之和、所有子数组的最大值之和
        for i in range(n):
            min_sum += (i - min_left[i]) * (min_right[i] - i) * nums[i]
            max_sum += (i - max_left[i]) * (max_right[i] - i) * nums[i]
        return max_sum - min_sum
