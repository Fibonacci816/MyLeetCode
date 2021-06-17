class Solution:
	# 先排序再判断相邻元素是否相等 时间：O(nlogn) 空间：O(1)
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        pre = nums[0]
        for num in nums[1:]:
            if num == pre:
                return pre
            pre = num
        return None

    # 记录出现过的元素 时间：O(n) 空间：O(n)
    def findDuplicate2(self, nums: List[int]) -> int:
        visited = set()
        for num in nums:
            if num in visited:
                return num
            visited.add(num)
        return None

    # 看做链表，找链表环的起始位置 时间：O(n) 空间：O(1)
    def findDuplicate3(self, nums: List[int]) -> int:
    	s = q = nums[0]
        # 循环退出时快慢指针相遇
        while True:
            s = nums[s]
            q = nums[nums[q]]
            if s == q:
                break
        q = nums[0]
        # 循环退出时快慢指针都在环的开始位置
        while s != q:
            s = nums[s]
            q = nums[q]
        return s
