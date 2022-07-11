class Solution:
    # 排序
    # 时间O(nlogn) 空间O(1)
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums)//2]
    
    # Boyer-Moore 投票算法
    # 时间O(n) 空间O(1)
    def majorityElement(self, nums: List[int]) -> int:
        maj, cnt = 0, 0
        for num in nums:
            if cnt == 0:
                maj = num
            cnt += 1 if num == maj else -1
        return maj

    # 随机
    # 时间期望O(n) 空间O(1)
    def majorityElement(self, nums: List[int]) -> int:
        half_len = len(nums) / 2
        while True:
            candidate = random.choice(nums)  # 随机选择一个数作为候选
            if sum(num == candidate for num in nums) > half_len:
                return candidate