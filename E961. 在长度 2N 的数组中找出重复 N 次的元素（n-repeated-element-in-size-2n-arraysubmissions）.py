class Solution:
    # 哈希表
    # 时间O(n) 空间O(n)
    def repeatedNTimes(self, nums: List[int]) -> int:
        visited = set()
        for num in nums:
            if num in visited:
                return num
            visited.add(num)

    # 随机
    # 时间期望O(1) 空间O(1)
    def repeatedNTimes(self, nums: List[int]) -> int:
        n = len(nums)
        # 期望 44 次结束循环
        while True:
            i, j = random.randrange(n), random.randrange(n)
            if i != j and nums[i] == nums[j]:
                return nums[i]

    # 数学（反证法可证明不存在相邻重复元素的间隔都大于2的数组）
    # 时间O(n) 空间O(1)
    def repeatedNTimes(self, nums: List[int]) -> int:
        n = len(nums)
        for gap in range(1, 4):
            for i in range(n-gap):
                if nums[i] == nums[i+gap]:
                    return nums[i]